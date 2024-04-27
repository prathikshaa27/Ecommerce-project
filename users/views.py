from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import SellerSignupSerializer, BuyerSignupSerializer, SigninSerializer, ProfileSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.serializers import SellerSignupSerializer

@api_view(['POST'])
def seller_signup(request):
    serializer = SellerSignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Seller signup successful'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def buyer_signup(request):
    serializer = BuyerSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response({'message': 'Buyer account created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def seller_signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_seller:
            login(request, user)
            return Response({'message': 'Seller logged in successfully'})
        else:
            return Response({'error': 'Invalid email or password for seller'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def buyer_signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and not user.is_seller:
            login(request, user)
            return Response({'message': 'Buyer logged in successfully'})
        else:
            return Response({'error': 'Invalid email or password for buyer'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
