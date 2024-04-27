from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(blank=False, null=False)
  order_status = models.CharField(max_length=50)
