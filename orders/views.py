# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Order
# from .serializers import OrderSerializer
# from rest_framework.permissions import AllowAny, IsAdminUser
# from products.models import Product

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

# # Buyer views
# @api_view(['GET'])
# @permission_classes([AllowAny])  
# def buyer_cart(request):
#     buyer_cart = request.session.get('cart', {})
#     product_ids = buyer_cart.keys()
#     buyer_products = Product.objects.filter(id__in=product_ids)
#     serializer = ProductSerializer(buyer_products, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def place_order(request):
#     request.session['cart'] = {}
#     return Response({'message': 'Order placed successfully'})
