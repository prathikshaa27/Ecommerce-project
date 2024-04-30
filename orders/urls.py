from django.urls import path
from orders import views

urlpatterns = [
    path('customer/display/products/', views.view_cart, name='cart_view'),
    path('customer/place/order/', views.place_order, name='place_order'),
]

