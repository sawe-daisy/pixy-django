from django.db import models
impor datetime as dt
# Create your models here.

class Image(models.Model):
    image=models.CharField()
    name=models.CharField(max_length=10)
