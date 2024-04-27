from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
def list_products_buyers(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    cart_key = 'cart'
    if cart_key not in request.session:
        request.session[cart_key] = {}
    
    cart = request.session[cart_key]
    cart[str(pk)] = {
        'product_id': pk,
        'product_name': product.product_name,
        'amount': str(product.amount),
    }
    
    request.session.modified = True
    return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def remove_from_cart(request, pk):
    cart_key = 'cart'
    if cart_key in request.session and str(pk) in request.session[cart_key]:
        del request.session[cart_key][str(pk)]
        request.session.modified = True
        return Response({'message': 'Product removed from cart'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Product not found in cart'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAdminUser])    
def view_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_product(request):
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def product_details(request,pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error':'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

