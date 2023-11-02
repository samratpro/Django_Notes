from django.db import models

# Create your models here.

class Logo(models.Model):
    logo_img = models.ImageField(upload_to='images/')
    icon_img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return 'Logo'
