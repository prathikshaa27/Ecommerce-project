from django.db import models
from users.models import CustomUser
from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product_name= models.ForeignKey(Product, on_delete=models.CASCADE,db_column="product_id")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
