from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from users.serializers import UserSerializer
from rest_framework.request import Request


@api_view(['POST'])
def signup(request:Request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        if user.is_seller:
            return Response({'message': 'Seller account created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Buyer account created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        if user.is_seller:
            return Response({'message': 'Seller logged in successfully'})
        else:
            return Response({'message': 'Buyer logged in successfully'})
    else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
