from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def view_cart(request):
 if request.method == 'GET':
  cart=request.session.get('cart', {})
  product_ids = [int(product_id) for product_id in cart.keys()]
  products = Product.objects.filter(pk__in=product_ids)
  serializer = ProductSerializer(products, many=True)
 return Response(serializer.data)

@api_view(['POST'])
def place_order(request):
    if request.method == 'POST':
        data = request.data
        if isinstance(data, list):
            serializer = OrderSerializer(data=data, many=True)
        else:
            serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            request.session.pop('cart', None)  
            return Response({'message': 'Order placed successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# # Seller views
# @api_view(['GET'])
# @permission_classes([IsAdminUser])  
# def seller_orders(request):
#     seller_products = Product.objects.filter(user=request.user)
#     orders = Order.objects.filter(product_name__in=seller_products)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def update_order_status(request, order_id):
#     try:
#         print("Order ID:", order_id)
#         print("User:", request.user)

#         order = Order.objects.get(pk=order_id, product_name__user=request.user)
#         print("Found Order:", order)

#         if 'order_status' in request.data:
#             order.order_status = request.data['order_status']
#             order.save()
#             return Response({'message': 'Order status updated successfully'})
#         else:
#             return Response({'error': 'Please provide the updated order status'}, status=status.HTTP_400_BAD_REQUEST)

#     except Order.DoesNotExist:
#         print("Order not found")
#         return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
