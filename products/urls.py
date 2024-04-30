from django.urls import path
from .views import list_products, manage_cart,filter_products

urlpatterns =[
    # path('products/',view_products),
     #path('products/add/', add_product),
    # path('products/<int:pk>/',product_details),
     #path('products/add/', add_product),
    path('customers/products/', list_products, name='list_products'),
    path('customers/cart/<int:product_id>/', manage_cart, name='manage_cart'),
    path('customers/filter/products/',filter_products, name='filter_products')
]