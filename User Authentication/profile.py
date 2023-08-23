# Model.py ------------------------
```
delete db migrations or db
delete db
then delete all files from the migration folder of the app folder without __init__.py
```


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_chat_limit = models.DecimalField(decimal_places=2, max_digits=10, default=3.0)
    question_limit = models.DecimalField(decimal_places=2, max_digits=10, default=20.0)
    monthly_question_limit = models.DecimalField(decimal_places=2, max_digits=10, default=620.0)
    

    def __str__(self):
        return self.user.username
    
# Signal to automatically create UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to save the UserProfile when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
