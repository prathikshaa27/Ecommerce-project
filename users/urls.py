from django.urls import path
from users import views

urlpatterns = [
    path('api/seller/signup/', views.seller_signup, name='seller_signup'),
    path('api/buyer/signup/', views.buyer_signup, name='buyer_signup'),
    path('api/seller/signin', views.seller_signin, name='seller_signin'),
    path('api/buyer/signin', views.buyer_signin, name='buyer_signin')
]
