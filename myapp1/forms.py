from django import forms
from .models import Image
from .models import AudioFile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'file')


class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['audio_file']