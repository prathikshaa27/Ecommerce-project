from django.urls import path
from .views import customer_signup, customer_signin, customer_details, customer_logout

urlpatterns = [
    path("api/customer/signup/", customer_signup),
    path("api/customer/signin/", customer_signin),
    path("api/profile/", customer_details),
    path("api/logout/", customer_logout)
]
 