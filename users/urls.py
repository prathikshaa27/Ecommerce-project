from django.urls import path
from .views import customer_signup, customer_signin, customer_details

urlpatterns = [
    # path('api/seller/signup/', seller_signup),
    # path('api/seller/signin/', seller_signin),
    path("api/customer/signup/", customer_signup),
    path("api/customer/signin/", customer_signin),
    path("api/profile/", customer_details),
]
