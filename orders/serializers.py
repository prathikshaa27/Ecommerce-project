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

from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'items']

from rest_framework import serializers
from .models import Order, OrderItem
from users.serializers import CustomUserSerializer  
from products.serializers import ProductSerializer  

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()  
    product_image_url = serializers.SerializerMethodField() 
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user_name', 'total_amount', 'status', 'product_image_url', 'items']

    def get_user_name(self, obj):
        return obj.user.username

   
    def get_product_image_url(self, obj):
        first_item = obj.items.first()
        if first_item and first_item.product:
            return first_item.product.image_url
        else:
            return None  
