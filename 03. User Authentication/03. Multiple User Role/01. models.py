from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission, Group
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_teacher(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_teacher', True)
        return self.create_user(email, password, **extra_fields)

    def create_student(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_student', True)
        return self.create_user(email, password, **extra_fields)

class AppUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='assigned_tasks')
    created_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='created_tasks')

class TeacherGroup(Group):
    class Meta:
        proxy = True

class StudentGroup(Group):
    class Meta:
        proxy = True

class TaskPermission(Permission):
    class Meta:
        proxy = True
        default_permissions = ()
        permissions = (
            ('can_create_task', 'Can create task'),
            ('can_remove_student', 'Can remove student'),
        )
