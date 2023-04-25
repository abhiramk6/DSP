from django.shortcuts import render, redirect

# Create your views here.

from .forms import ImageForm
from .models import Image

from .models import AudioFile
from .forms import AudioFileForm


from django.http import HttpResponse
from django.http import FileResponse

from django.conf import settings
from django.shortcuts import get_object_or_404

import os
from django.db.models import Model
# from rembg import remove
import cv2

from gtts import gTTS


def home(request):
    return render(request,'home.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
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


# def rmbg_image(request, image_id):
#     x=Image.objects.count()
#     image = get_object_or_404(Image, pk=x)
#     file_path = image.file.path
#     im = cv2.imread(file_path)
#     rmbgimage = remove(im)
#     ff=file_path.split(".")
#     file_path1=ff[0]+"_rmbg.png"
#     print(file_path)
#     print(file_path1)

#     cv2.imwrite(file_path1,rmbgimage)

#     if os.path.isfile(file_path1):
#         with open(file_path1, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='image/jpeg')
#             response['Content-Disposition'] = 'attachment; filename=' + image.title
#             return response
#     else:
#         return render(request, 'nofileexists.html')
        

def audio_upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio_upload')
    else:
        form = AudioFileForm()

    audio_files = AudioFile.objects.all()

    return render(request, 'audio_upload.html', {'form': form, 'audio_files': audio_files})

def audio_download(request, pk):
    x=AudioFile.objects.count()
    audio_file = AudioFile.objects.get(pk=x)
    response = FileResponse(audio_file.audio_file)
    response['Content-Disposition'] = f'attachment; filename="{audio_file.audio_file.name}"'
    return response

    

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST['text']
        language = 'en'
        tts = gTTS(text=text, lang=language)
        tts.save('static/audio/tts_audio.mp3')
        # os.system('start tts_audio.mp3') # On Windows
    audio_file = 'tts_audio.mp3'
    context = {'audio_file': audio_file}    
    return render(request, 'text_to_speech.html',context)

def download_ttsaudio(request):
    fname="./static/audio/tts_audio.mp3"
    f = open(fname,"rb") 
    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] ='audio/mp3'
    response['Content-Disposition'] = f'attachment; filename="tts_audio.mp3"'
    return response





