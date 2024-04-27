from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def seller_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def buyer_orders(request):
    user = request.user
    orders = Order.objects.filter(buyer = user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_order_status(request, order_id):
    try:
        order = Order.objects.get(pk =order_id)
    except Order.DoesNotExist:
        return Response({'order':'Order does not exist'}, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        order_status = request.data.get('order_status')
        if order_status:
            order.order_status=order_status
            order.save()
            return Response({'message':'Order status updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'order:Order status required'},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
