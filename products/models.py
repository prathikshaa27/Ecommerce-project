from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=100, blank=False, null= False)
    image_url = models.URLField(blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank= False, null=False)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE )
        
