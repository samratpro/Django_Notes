from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.admin import UserAdmin
from .models import AppUser  # Replace with your custom user model

# @admin.register(AppUser)
# class UserAdmin(UserAdmin):
#     """Define admin model for custom User model with no email field."""

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'activation_code', 'password_reset_code', 'profile_image', 'credit')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         )
#     add_fieldsets = ((None, {'classes': ('wide',),'fields': ('email', 'password1', 'password2'),}),)
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)


admin.site.register(AppUser)
# Changing the Django Admin Header Text
admin.site.site_header = 'AI Writing Project'   

# 'profile_image', 'activation_code', 'credit', 'password_reset_code'  THESE ARE CUSTOM FIELDS HERE



