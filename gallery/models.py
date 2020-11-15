from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.location

class Category(models.Model):
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Image(models.Model):
    name=models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    location= models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    pub_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





