from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # The default 'auth.User' model already has 'groups' and 'user_permissions' fields.
    # When you inherit from 'AbstractUser', you inherit these fields, which can lead to conflicts
    # when defining your custom User model. To avoid these conflicts, we need to define custom related_name.

    # Adding related_name to the 'groups' field to avoid reverse accessor clash with the default 'auth.User.groups'.
    # The 'related_name' defines the reverse relation from the 'Group' model to the 'User' model.
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='custom_user_set',  # Custom related name to avoid clashes
        blank=True
    )

    # Similarly, adding related_name to the 'user_permissions' field to avoid reverse accessor clash with 'auth.User.user_permissions'.
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='custom_user_permissions_set',  # Custom related name to avoid clashes
        blank=True
    )

    def __str__(self):
        return self.username
    

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    target_amount = models.IntegerField(blank=True, null=True)
    target_date = models.DateField(blank=True, null=True)

    # This 'manager' field is a ForeignKey to the 'User' model, representing the group manager.
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_groups')
    
    # The 'members' field is a ManyToManyField between 'Group' and 'User' models.
    # Without a custom related_name, this would clash with the 'groups' field in the User model.
    # Adding a custom related_name for the reverse relationship from 'User' to 'Group' to avoid conflicts.
    members = models.ManyToManyField(User, related_name='group_memberships', blank=True)

    def __str__(self):
        return self.name
