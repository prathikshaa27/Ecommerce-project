from django.urls import path
from .views import (
    list_products,
    manage_cart,
    list_categories,
    list_products_by_categories,
)

urlpatterns = [
    # path('products/',view_products),
    # path('products/add/', add_product),
    # path('products/<int:pk>/',product_details),
    # path('products/add/', add_product),
    path("api/categories/products/", list_products, name="list_products"),
    path("api/cart/<int:product_id>/", manage_cart, name="manage_cart"),
    path("api/categories/", list_categories, name="list_categories"),
    path(
        "api/categories/<int:category_id>/",
        list_products_by_categories,
        name="category_list",
    ),
]
