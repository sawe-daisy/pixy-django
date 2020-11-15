from django.db import models
import datetime as dt
# Create your models here.

class Image(models.Model):
    name=models.CharField(max_length=10)
