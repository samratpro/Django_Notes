# Import files
from django.db import models           # --------------------------------------------------------- # Global
from django.utils.text import slugify  # --------------------------------------------------------- # For Slug
from django.utils import timezone      # --------------------------------------------------------- # For django server time


# Example Model for Blog Post
class PostCetgory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super().save(*arg, **kwargs)

class BlogPost(models.Model):
    post_serial = models.AutoField(primary_key=True)                   # Auto-incrementing serial number, 1,2,3,4,5,6....
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)   # separating User accroding to authenticate
    category = models.ForeignKey(PostCetgory, on_delete=models.SET_NULL, null=True, blank=True)   # If user will delete, category never delete
    feature_img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)    # automatically current date & time when a new instance of the model is created
    expire_date = models.DateField(default=timezone.now)  # timezone.now `date` vs timezone.now() `date and time`
    modified_date = models.DateField(auto_now=True)   # Similar to auto_now_add, it's used with DateTimeField. It track the last updated 
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)


#  Each book can have only one author, but an author can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)  # If author delete All associate Book will delete
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, blank=True)   # If author delete associate Book will remain


# each Profile is linked to exactly one User, and each User has only one Profile.
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#  Each Course can have multiple Students enrolled, and each Student can take multiple Courses.
class Student(models.Model):
    name = models.CharField(max_length=100)
class Course(models.Model):
    students = models.ManyToManyField(Student)










# # For JSON Field only
# import jsonfield


# # Create your models here.
# class KeywordData(models.Model):
#     List_Name = models.CharField(max_length=15, null=True)
#     keywords = jsonfield.JSONField(null=True)


#     def __str__(self):
#         return self.List_Name
