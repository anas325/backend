from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
    

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    target_amount = models.IntegerField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_groups')
    members = models.ManyToManyField(User, related_name='groups', blank=True)

    def __str__(self):
        return self.name
    
