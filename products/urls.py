from django.urls import path
from .views import (
    list_products,
    manage_cart,
    list_categories,
    list_products_by_categories,
    search_products,
    product_detail,
    category_price_filter
)

urlpatterns = [
    path("api/categories/products/", list_products, name="list_products"),
    path("api/cart/<int:product_id>/", manage_cart, name="manage_cart"),
    path("api/categories/", list_categories, name="list_categories"),
    path(
        "api/categories/<int:category_id>/",
        list_products_by_categories,
        name="category_list"),
    path('api/search/', search_products, name='search_products'),
    path('api/products/<int:product_id>/', product_detail, name='product-detail'),
     path('api/category-price-filter/', category_price_filter, name='category_price_filter'),

   
    
]
