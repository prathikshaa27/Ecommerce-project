from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from .models import Order, OrderItem
from .serializers import OrderSerializer
from users.serializers import ProfileSerializer
from rest_framework import status
from products.models import Product
from users.models import CustomUser, Profile
from django.core.exceptions import ObjectDoesNotExist
from users.models import Profile
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPagination

@api_view(['GET'])
@login_required
def view_cart(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total_amount = 0

    for product_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        quantity = item_data['quantity']
        amount = float(item_data['amount'])
        total_amount += quantity * amount
        cart_items.append({
            "product_id": product_id,
            "product_name": product.product_name,
            "amount": amount,
            "quantity": quantity,
            "image_url": product.image_url 
        })

    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(cart_items, request)
    return paginator.get_paginated_response({"cart_items": result_page, "total_amount": total_amount})

@api_view(['POST'])
@login_required
def place_order(request):
    try:
        user = request.user  
        cart = request.session.get("cart", {})
        order = Order.objects.create(user=user)
        
        total_amount = 0
        for product_id, item_data in cart.items():
            product = Product.objects.get(pk=product_id)
            quantity = item_data['quantity']
            price = float(item_data['amount'])
            total_amount += quantity * price
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
        
        order.total_amount = total_amount
        order.save()
        
        request.session['cart'] = {}
        serializer = OrderSerializer(order)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@login_required
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(orders, request)
    serializer = OrderSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
