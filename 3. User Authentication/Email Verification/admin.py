from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser  # Replace with your custom user model


# This for viewing custom user in admin panel

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'profile_image', 'activation_code')}),   # profile_image is custom field here
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(AppUser, CustomUserAdmin)
