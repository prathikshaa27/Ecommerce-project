from django.urls import path
from orders import views

urlpatterns = [
    path('api/orders/', views.cart_and_order, name='cart_and_order'),
    
]
