from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class AppUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    activation_code = models.CharField(max_length=50, blank=True, null=True)
    password_reset_code = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    credit = models.IntegerField(default=0)
    # is_active = models.BooleanField(default=False)
    
    # Specify related_name for groups and user_permissions to resolve the clash
    groups = models.ManyToManyField(Group, related_name='app_users')
    user_permissions = models.ManyToManyField(Permission, related_name='app_users')

    def activate(self):
        self.is_active = True
        self.activation_code = ''
        self.save()
        
