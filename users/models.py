from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)

    class Meta:
        db_table = "Users"


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    mobile = models.CharField(max_length=20, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    pincode = models.CharField(max_length=7, blank=False, null=False, default='')
    addresses = models.JSONField(default=list)
