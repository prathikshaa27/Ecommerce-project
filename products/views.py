from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductCategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .models import Product, ProductCategory


@api_view(["GET"])
@login_required
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@login_required
def list_categories(request):
    categories = ProductCategory.objects.all()
    serializer = ProductCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'DELETE'])
@login_required
def manage_cart(request, product_id):
    if request.method == "POST":
        try:
            product = get_object_or_404(Product, pk=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        cart_key = "cart"
        if cart_key not in request.session:
            request.session[cart_key] = {}

        cart = request.session[cart_key]
        quantity = int(request.data.get('quantity', 1))  
        cart[str(product_id)] = {
            "product_id": product_id,
            "product_name": product.product_name,
            "amount": str(product.amount),
            "quantity": quantity,
        }

        request.session.modified = True
        return Response(
            {"message": "Product added to cart"}, status=status.HTTP_201_CREATED
        )
    elif request.method == "DELETE":
        cart = request.session.get("cart", {})
        if str(product_id) not in cart:
            return Response(
                {"error": "Product is not in the cart"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        del cart[str(product_id)]
        request.session["cart"] = cart
        return Response(
            {"message": "Product removed from cart"}, status=status.HTTP_200_OK
        )

@api_view(["GET"])
@login_required
def list_products_by_categories(request, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    products = Product.objects.filter(name=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@login_required
def search_products(request):
    search_query = request.query_params.get('q', '')
    if search_query:
        products = Product.objects.filter(product_name__icontains=search_query)
    else:
        products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def category_price_filter(request):
    if request.method == 'GET':
        category_name = request.query_params.get('category')
        min_price = float(request.query_params.get('min_price', 0))
        max_price = float(request.query_params.get('max_price', float('inf')))
        
        try:
            category = ProductCategory.objects.get(name=category_name)
            products = Product.objects.filter(name=category, amount__gte=min_price, amount__lte=max_price)
            serializer = ProductSerializer(products, many=True)
            
            response_data = {
                'products': serializer.data,
                'category': category_name,
                'min_price': min_price,
                'max_price': max_price
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        except ProductCategory.DoesNotExist:
            return Response({'error': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

