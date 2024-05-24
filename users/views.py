from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import logout
from .models import CustomUser, Profile
from users.serializers import BuyerSignupSerializer, BuyerSigninSerializer, ProfileSerializer, CustomUserSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.decorators import login_required


CustomUser = get_user_model()


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
        user = request.user
        profile = user.profile
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        user_serializer = CustomUserSerializer(user)
        profile_serializer = ProfileSerializer(profile)

        data = {
            "username": user_serializer.data["username"],
            "email": user_serializer.data["email"],
            "profile": {
                "mobile": profile_serializer.data["mobile"],
                "address":profile_serializer.data["address"],
                "addresses": profile_serializer.data["addresses"],
                "pincode": profile_serializer.data["pincode"]
            }
        }

        return Response(data)

    elif request.method == "PUT":
        user_serializer = CustomUserSerializer(user, data=request.data, partial=True)
        profile_data = request.data.get("profile", {})
        addresses_data = profile_data.get("addresses", [])  

        if not isinstance(addresses_data, list):
            addresses_data = []

        profile_serializer = ProfileSerializer(profile, data={
            "mobile": profile_data.get("mobile", profile.mobile),
            "address": profile_data.get("address", profile.address),
            "pincode": profile_data.get("pincode", profile.pincode),
            "addresses": addresses_data 
        }, partial=True)

        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return Response({"message": "Details updated successfully"}, status=status.HTTP_200_OK)
        else:
            errors = {}
            errors.update(user_serializer.errors)
            errors.update(profile_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["POST"])
def customer_logout(request):
    if request.method == "POST":
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

