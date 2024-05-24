from rest_framework import serializers
from .models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "image_url"]


class ProductSerializer(serializers.ModelSerializer):
    name_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(), source="name"
    )
    category_name = serializers.CharField(source="name.name")

    class Meta:
        model = Product
        fields = [
            "id",
            "user",
            "product_name",
            "image_url",
            "amount",
            "quantity",
            "description",
            "name_id",
            "category_name",
        ]
