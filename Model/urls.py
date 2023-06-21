from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('single_data/<data_id>', views.single_data, name='single_data'),  
    path('update_data/<data_id>', views.update_data, name='update_data'),  
]
