from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST', 'DELETE'])
def manage_cart(request, product_id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        cart_key = 'cart'
        if cart_key not in request.session:
            request.session[cart_key] = {}

        cart = request.session[cart_key]
        cart[str(product_id)] = {
            'product_id': product_id,
            'product_name': product.product_name,
            'amount': str(product.amount),
        }

        request.session.modified = True
        return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        cart = request.session.get('cart', {})
        if str(product_id) not in cart:
            return Response({'error': 'Product is not in the cart'}, status=status.HTTP_400_BAD_REQUEST)
        del cart[str(product_id)]
        request.session['cart'] = cart
        return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)

# @api_view(['GET'])  
# def view_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_product(request):
#     serializer = ProductSerializer(data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def product_details(request,pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({'error':'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
    

