from django.db import models

# Create your models here.


from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='images/')

