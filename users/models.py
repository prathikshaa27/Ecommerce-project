from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    pincode = models.CharField(max_length=7)

User.groups.field.remote_field.related_name = "custom_user_groups"
User.user_permissions.field.remote_field.related_name = "custom_user_permissions"
