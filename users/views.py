from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BuyerSignupSerializer, BuyerSigninSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# @api_view(['POST'])
# def seller_signup(request):
#     if request.method == 'POST':
#         serializer = UserSignupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(is_seller=True, is_superuser=True)  
#             return Response({'message': 'Seller signed up successfully!'})
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def seller_signin(request):
#     if request.method == 'POST':
#         serializer = UserSigninSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['username']
#             print(username,password)
#             user = authenticate(username=username, password=password)
#             print(user)
#             if user is not None and (user.is_seller):  
#                 login(request, user)
#                 return Response({'message': 'Seller signed in successfully!'})
#             return Response({'error': 'Invalid credentials or user is not a seller'}, status=400)
#         return Response(serializer.errors, status=400)

@api_view(['POST'])
def buyer_signup(request):
    if request.method == 'POST':
        serializer = BuyerSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response({'message': 'Buyer signed up successfully!'})
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def buyer_signin(request):
    if request.method == 'POST':
        serializer = BuyerSigninSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and not user.is_superuser:
                login(request, user)
                return Response({'message': 'Buyer signed in successfully!'})
            return Response({'error': 'Invalid credentials or user is not a buyer'}, status=400)
        return Response(serializer.errors, status=400)
