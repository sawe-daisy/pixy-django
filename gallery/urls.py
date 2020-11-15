from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views
from django.urls import path, re_path

urlpatterns=[
    path('', views.index, name='Images'),
    path('search/', views.search_category, name='searchResults'),
    path('image/', views.viewImage, name='viewImage')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)