from django.utils.translation import ugettext_lazy as _
from datetime import datetime,timedelta, timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise  ValueError("Users must have an email Address")
        if len(email) > 1000:
            raise  ValueError("Email Address must not exceed the length of 1000") 
        if not password:
            raise  ValueError("Password must be something")    
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password):
        if not email:
            raise  ValueError("Users must have an email Address")
        if len(email) > 1000:
            raise  ValueError("Email Address must not exceed the length of 1000") 
        if not password:
            raise  ValueError("Password must be something")    
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(verbose_name = "full_name",max_length = 1000)
    email = models.EmailField(verbose_name = "email",max_length = 1000,unique = True)
    date_joined = models.DateTimeField(verbose_name = "Date joined",auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = "Last Login",auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    
    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj = None):
        return self.is_active
    def has_module_perms(self,app_Label):
        return True    
