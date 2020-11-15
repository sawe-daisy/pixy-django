from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls.static import settings
from . import views
from django.urls import path, re_path

urlpatterns=[
    # path('search/', views.searchResults, name='searchResults'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)