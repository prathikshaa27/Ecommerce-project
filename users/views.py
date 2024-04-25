from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from users.models import Profile 
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        address = data.get('address')
        mobile = data.get('mobile')
        pincode = data.get('pincode')
        is_seller = data.get('is_seller', False)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        
        profile = Profile.objects.create(
            user=user,
            mobile=mobile,
            address=address,
            pincode=pincode
        )
        
        if is_seller:
            user.is_staff = True  
            user.save()
        
        login(request, user)
        
        if is_seller:
            return JsonResponse({'message': 'Seller account created successfully'})
        else:
            return JsonResponse({'message': 'Buyer account created successfully'})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return JsonResponse({'message': 'Seller logged in successfully'})
            else:
                return JsonResponse({'message': 'Buyer logged in successfully'})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
