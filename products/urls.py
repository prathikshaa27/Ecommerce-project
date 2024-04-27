from django.urls import path
from .views import list_products_buyers, add_product, product_details, add_to_cart, remove_from_cart,view_products

urlpatterns =[
    path('products/',view_products),

    path('products/add/', add_product),
    path('products/<int:pk>/',product_details),
    path('buyer/products/', list_products_buyers),
    path('buyer/cart/add/<int:pk>',add_to_cart ),
    path('buyer/cart/remove/<int:pk>',remove_from_cart)
]