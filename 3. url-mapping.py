# URL Mapping in Project URL file-------------------
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('NewApp.urls')),
]  # NewApp is App name here...



# URL Mapping in App URL file----------------------
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('contactus', views.contactus, name='contactus'),  
    path('article', views.article, name='article'),  
    path('about', views.about, name='about'),  
]
# Home is function name here...
# >>> 404.html and Debug is false for 404 page
