from django.urls import path
from users.views import signup, signin

urlpatterns  =[
    path('api/signup', signup, name='signup'),
    path('api/signin', signin, name='signin')
]
