from django.urls import path
from orders import views

urlpatterns = [
    # Seller URLs
    path('api/seller/orders/', views.seller_orders, name='seller_orders'),
    path('api/seller/orders/<int:order_id>/update/', views.update_order_status, name='update_order_status'),

    # Buyer URLs
    path('api/buyer/cart/', views.buyer_cart, name='buyer_cart'),
    path('api/buyer/place_order/', views.place_order, name='place_order'),
]
