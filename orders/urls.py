from django.urls import path
from orders.views import seller_orders, buyer_orders,update_order_status

urlpatterns =[
    path('api/seller/orders', seller_orders, name='seller_orders'),
    path('api/buyers/orders', buyer_orders, name='buyer_orders'),
    path('api/order/<int:order_id>/', update_order_status, name='update_order_status')
]