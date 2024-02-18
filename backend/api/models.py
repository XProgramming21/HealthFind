from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,login,password=None):
        if not login:
            raise ValueError('User must have login')
        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,login,password):
        user = self.create_user(login,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)   

class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=8, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    

    def get_full_name(self):
        return self.login

    def get_short_name(self):
        return self.login

    def __str__(self):
        return self.login
