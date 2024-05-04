from django.urls import path
from orders import views

urlpatterns = [
    path("api/view_cart/", views.view_cart, name="Cart"),
    path("api/orders/", views.place_order, name="Place_Order")
]
