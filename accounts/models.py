# from django.db import models
# # from django.contrib.auth.forms import UserCreationForm

# # Create your models here.
# class Registration(models.Model):
#     username = models.CharField(max_length=25, default=None)
#     password = models.CharField(max_length=25, default=None)
#     email = models.EmailField()
#     is_verified = models.BooleanField(default=False)
#     token = models.CharField(max_length=100,default=None)

# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Registration(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  
    is_admin = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)  
    token = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser