from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, upload_image, original_image, gray_image, rotated_image, audio_upload, audio_download, text_to_speech,download_ttsaudio
# from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('image/', upload_image, name='upload_image'),
    path('original-image/<int:image_id>/', original_image, name='original-image'),
    path('gray-image/<int:image_id>/', gray_image, name='gray-image'),
    path('rotated-image/<int:image_id>/', rotated_image, name='rotated-image'),
    # path('rmbg-image/<int:image_id>/', rmbg_image, name='rmbg-image'),
    path('audio/upload/', audio_upload, name='audio_upload'),
    path('audio/download/<int:pk>/', audio_download, name='audio_download'),
    path('tts/', text_to_speech, name='text_to_speech'),
    path('audio/download/', download_ttsaudio, name='download_ttsaudio'),
    ]