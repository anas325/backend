from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=False)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    organizer = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='organized_events')
    participants = models.ManyToManyField('users.User', related_name='events', blank=True)
    target_amount = models.IntegerField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=150, unique=False)
    description = models.CharField(max_length=255, unique=False)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'),
                                                    ('completed', 'Completed')], default='pending')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')
    
    
    def __str__(self):
        return self.title


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return f"{self.event.name} - {self.amount}"