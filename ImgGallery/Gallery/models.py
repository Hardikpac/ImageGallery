from django.db import models

# Create your models here.
class Images(models.Model):
    photo = models.ImageField(upload_to='myimg')
    date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=140)
