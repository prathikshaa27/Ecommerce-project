from django.db import models
from users.models import CustomUser

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, blank=False, null=False)
    image_url = models.URLField(blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
