# -*- encoding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from login_test.settings import settings

# Create your models here.

def user_filename(self, filename):
    url = "accounts_picture/%s/%s" % (self.id, filename)
    return url

# Create your models here.
#-- Create_user extendido de AbstractBaseUser
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
 #       print(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
            is_active=True,
            is_superuser=True,
            is_staff=True
        )
        user.set_password(password)
        user.save()
        return user
 

#-- Clase abstracta extendida del modelo User
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    #-- Atributos adicionales
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'users'
        ordering = ['email',]


#-- Clase extendia del User para control de las llaves de activacion (Activacion / Solicitud de Contraseña / Invitacion)
class UserRequest(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #-- Keys para la validacion por email cuando de crea el usuario
    activation_key = models.CharField(max_length=40, blank=True)
    expires_key = models.DateTimeField(default=datetime.now)
#    activation_type = models.CharField(max_length=2, choices=ut.ACTIVATION_CHOICES, default='1')
#    activation_status = models.CharField(max_length=2, choices=ut.ACTIVATIONSTATUS_CHOICES, default='0')
    activation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users_request'
