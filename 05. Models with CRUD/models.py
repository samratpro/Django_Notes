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
    category = models.ForeignKey(PostCetgory, on_delete=models.SET_NULL, null=True, blank=True)   # separating User accroding to authenticate
    feature_img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateField(default=timezone.now)  # timezone.now `date` timezone.now() `date and time`
    modified_date = models.DateField(auto_now=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)











# # For JSON Field only
# import jsonfield


# # Create your models here.
# class KeywordData(models.Model):
#     List_Name = models.CharField(max_length=15, null=True)
#     keywords = jsonfield.JSONField(null=True)


#     def __str__(self):
#         return self.List_Name
