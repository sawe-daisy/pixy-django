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
    image=models.ImageField(upload_to='images/')
    description = models.CharField(max_length=50)
    location= models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    pub_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pic=cls.objects.get(id=id)
        return pic

    @classmethod
    def filter_by_category(cls, category):
        pics=cls.objects.filter(category__category__icontains=category)
        return pics

    @classmethod
    def search_image(cls,category):
        pics= cls.objects.filter(category__category__icontains=category)
        return pics
    
    @classmethod
    def filter_by_location(cls, location):
        pics=cls.objects.filter(location__location__icontains=location)
        return pics



