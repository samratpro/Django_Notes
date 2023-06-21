from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),   
    path('alldata', views.alldata, name='alldata'),
    path('single_data/<website_id>', views.update_website, name='single_data'),  
    path('update_data/<website_id>', views.update_website, name='update_data'),  
]
