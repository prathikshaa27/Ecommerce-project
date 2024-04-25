from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=50)