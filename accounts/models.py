from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid4
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render



def get_file_path_user(instance, filename):
    uuid_name = uuid4().hex
    return '/'.join(['user_profile/', uuid_name])




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    profile_pic = models.ImageField(upload_to=get_file_path_user, default='user_profile/usrDefaultImage.png')
    filename = models.CharField(max_length=64, null=True)
    
    intro = models.CharField(max_length=100, blank=True, null=True, default="")
    email = models.CharField(max_length=100, blank=True, null=True)
    #없앨거에요?
    nickname = models.CharField(max_length=10)

    #이멜인증
    dgupass = models.ImageField(upload_to=get_file_path_user, null=False, blank=False, default=False)
    dgupass_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    


