from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.
def index(request):
    images= Image.objects.all().order_by('-id')
    animals=Image.filter_by_category('Pets')
    travel=Image.filter_by_category('Travel')
    food=Image.filter_by_category('Food')
    random=Image.filter_by_category('Random')
    title = 'Pix Bay'
    return render(request, 'index.html', {"title": title, "images": images, "animals": animals,
    "travel": travel, "food": food, "random":random})

def search_category(request):
    if 'images' in request.GET and request.GET['images']:
        cateGory=request.GET.get('images')
        imagesFound=Image.search_image(cateGory)
        message=f"{cateGory}"
        
        return render(request, "search.html", {"message": message,"imagesFound": imagesFound})

    else:
        message ="Item searched is unavailable "
        return render(request, 'search.html', {"message": message})

# def search_location(request):
#     if 'location' in request.GET and request.GET['location']:
#         locationTerm=request.GET.get('location')
#         imagesFound=Image.filter_by_location(locationTerm)
#         message = f"{locationTerm}"

#         return render(request, '')

def viewImage(request,id ):
    image=Image.get_image_by_id(id)
    if image:
        return render(request, "pics.html", {"image": image})
    else:
        return redirect(index)