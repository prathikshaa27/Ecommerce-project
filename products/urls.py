from django.urls import path
from .views import list_products, add_product, product_details

urlpatterns =[
    path('products/',list_products),
    path('products/add/', add_product),
    path('products/<int:pk>/',product_details)
]