
# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(null=True, max_length=200)
    Email = models.CharField(null=True, max_length=200)
    Phone = models.CharField(null=True, max_length=200)
    Account_No = models.CharField(null=True, max_length=200)
    Debit_Card_No = models.CharField(null=True, max_length=200)

    Exp_Date = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)
    profile_pics = models.ImageField(
        default="unknown.png", null=True, blank=True)
    def __str__(self):
    	return str(self.user)


class Post_all(models.Model):
    mode=(('public','PUBLIC'),('private', 'PRIVATE'),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=5000)

    Date = models.DateField(auto_now_add=True)
    Picture = models.FileField(upload_to="user_Image", blank=True)
    Mode = models.CharField(max_length=7, choices=mode, default='PUBLIC')

    def __str__(self):
        return str(self.user)


class Post_public(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=5000)

    Date = models.DateField(auto_now_add=True)
    Picture = models.ImageField(upload_to="user_Image", blank=True)


    def __str__(self):
        return str(self.user)

class Post_private(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.CharField(max_length=5000)

    Date = models.DateField(auto_now_add=True)
    Picture = models.ImageField(upload_to="user_Image", blank=True)


    def __str__(self):
        return str(self.user)
