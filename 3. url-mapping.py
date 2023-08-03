# URL Mapping in Project URL file-------------------
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NewApp.urls'))
]  # NewApp is App name here...



# URL Mapping in App URL file----------------------
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),  
    path('contactus', views.contactus, name='contactus'),  
    path('article', views.article, name='article'),  
    path('about', views.about, name='about'),  
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # for collctstatic or admin css
# >>> 404.html and Debug is false for 404 page
