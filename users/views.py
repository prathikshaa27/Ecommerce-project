from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BuyerSignupSerializer, BuyerSigninSerializer, CustomUserSerializer
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.decorators import login_required
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


@api_view(["POST"])
def customer_signup(request):
    if request.method == "POST":
        serializer = BuyerSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer signed up successfully!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def customer_signin(request):
    if request.method == "POST":
        serializer = BuyerSigninSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None and not user.is_superuser:
                login(request, user)
                request.session["user_id"] = user.id
                next_url = request.GET.get("next", None)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return Response({"message": "Customer signed in successfully!"},status=status.HTTP_200_OK)

            return Response(
                {"error": "Invalid credentials or user is not a customer"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT"])
@login_required
def customer_details(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)