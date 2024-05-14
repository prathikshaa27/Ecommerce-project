from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Order
from .serializers import OrderSerializer
from users.serializers import ProfileSerializer
from rest_framework import status
from products.models import Product
from users.models import CustomUser,Profile
from django.core.exceptions import ObjectDoesNotExist
from users.models import Profile
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def view_cart(request):
    if request.method == 'GET':
        cart = request.session.get('cart', {})
        product_ids = [int(product_id) for product_id in cart.keys()]
        products = Product.objects.filter(pk__in=product_ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@login_required
def place_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Order placed successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@login_required
def user_orders(request):
    user_id = request.user.id
    print(type(user_id))
    orders = Order.objects.filter(user_id=user_id)
    print(orders)
    serializer = OrderSerializer(orders, many=True)
    print(serializer)
    return Response(serializer.data)




