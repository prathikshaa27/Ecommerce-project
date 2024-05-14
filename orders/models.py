from django.db import models
from users.models import CustomUser
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product_id")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_transit')

    def __str__(self):
        return f"Order {self.pk} - {self.status}"
