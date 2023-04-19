from django.shortcuts import render

# Create your views here.

from .forms import ImageForm

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Image
import os
from django.db.models import Model

import cv2





# def home(request):
#     return render(request,'home.html',{'name':'Sandeep'})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    
    return render(request, 'upload_image.html', {'form': form})


def original_image(request, image_id):
    x=Image.objects.count()
    image = get_object_or_404(Image, pk=x)
    file_path = image.file.path

    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=' + image.title
            return response
    else:
        return render(request, 'nofileexists.html')


def gray_image(request, image_id):
    x=Image.objects.count()
    image = get_object_or_404(Image, pk=x)
    file_path = image.file.path
    im = cv2.imread(file_path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ff=file_path.split(".")
    file_path1=ff[0]+"_gray.png"
    print(file_path)
    print(file_path1)

    cv2.imwrite(file_path1,gray)

    if os.path.isfile(file_path1):
        with open(file_path1, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=' + image.title
            return response
    else:
        return render(request, 'nofileexists.html')


def rotated_image(request, image_id):
    x=Image.objects.count()
    image = get_object_or_404(Image, pk=x)
    file_path = image.file.path
    im = cv2.imread(file_path)
    rotimage = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
    ff=file_path.split(".")
    file_path1=ff[0]+"_rot.png"
    print(file_path)
    print(file_path1)

    cv2.imwrite(file_path1,rotimage)

    if os.path.isfile(file_path1):
        with open(file_path1, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename=' + image.title
            return response
    else:
        return render(request, 'nofileexists.html')
        

