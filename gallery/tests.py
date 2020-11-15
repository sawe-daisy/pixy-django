from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class Test_image(TestCase):

    def setUp(self):
        self.image=Image(name='name', image='image', 
        description='description')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    
    def tearDown(self):
        Image.objects.all().delete()

class Location_Test(TestCase):

    def setUP(self):
        self.location=Location(location='location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
    
    def tearDown(self):
        Location.objects.all.delete()

class Category_Test(TestCase):
    
    def setUP(self):
        self.location=Location(location='location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
    
    def tearDown(self):
        Location.objects.all.delete()