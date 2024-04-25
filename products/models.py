from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE )
        
