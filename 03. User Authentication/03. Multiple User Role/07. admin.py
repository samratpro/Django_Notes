from django.contrib import admin
from .models import AppUser, Teacher, Student

admin.site.register(AppUser)
admin.site.register(Student)
admin.site.register(Student)
admin.site.site_header = 'AI Writing Project'   
