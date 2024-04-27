from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  is_seller = models.BooleanField(default=False)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  mobile = models.CharField(max_length=20,blank=False, null=False)
  address = models.TextField(blank=False, null=False)
  pincode = models.CharField(max_length=7, blank=False, null=False)

User.groups.field.remote_field.related_name = "custom_user_groups"
User.user_permissions.field.remote_field.related_name = "custom_user_permissions"
