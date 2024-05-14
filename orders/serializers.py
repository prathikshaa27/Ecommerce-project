from rest_framework import serializers
from .models import Order
from products.models import Product
from users.models import CustomUser

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    name = serializers.CharField(source = "product_name.product_name",read_only=True)
    image_url = serializers.URLField(source = "product_name.image_url",read_only=True)


    class Meta:
        model = Order
        fields = ['user', 'product_name',"name","image_url"]

    def create(self, validated_data):
        username = validated_data.pop('user')
        product_id = validated_data.pop('product_name')
        user = CustomUser.objects.get(username=username)
        order = Order.objects.create(user=user, product_name=product_id)
        return order
