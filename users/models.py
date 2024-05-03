from django.db import models
from django.contrib.auth.models import AbstractUser


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
    pincode = models.CharField(max_length=7, blank=False, null=False)


# CustomUser.groups.field.remote_field.related_name = "custom_user_groups"
# CustomUser.user_permissions.field.remote_field.related_name = "custom_user_permissions"
