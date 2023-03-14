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
    path('', views.home, name='home')  
] # Home is function name here...
