from django.urls import path
from .views import buyer_signup, buyer_signin

urlpatterns = [
    #path('api/seller/signup/', seller_signup),
    #path('api/seller/signin/', seller_signin),
    path('api/customer/signup/', buyer_signup),
    path('api/customer/signin/', buyer_signin),
]
