from django.urls import path
from .views import upload_image, original_image, gray_image, rotated_image, rmbg_image
# from .views import home

urlpatterns = [
    # path('', home, name='upload_image'),
    path('', upload_image, name='upload_image'),
    path('original-image/<int:image_id>/', original_image, name='original-image'),
    path('gray-image/<int:image_id>/', gray_image, name='gray-image'),
    path('rotated-image/<int:image_id>/', rotated_image, name='rotated-image'),
    path('rmbg-image/<int:image_id>/', rmbg_image, name='rmbg-image'),
]