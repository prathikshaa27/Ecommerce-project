from django.urls import path
from orders import views

urlpatterns = [
    path('api/view_cart/',views.view_cart,name="Cart"),
    path("api/orders/", views.place_order, name="Cart"),
    path('api/view_orders/', views.user_orders, name="Display_orders")

]
