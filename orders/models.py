from django.db import models
from users.models import CustomUser
from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)
    order_status = models.CharField(max_length=50)
