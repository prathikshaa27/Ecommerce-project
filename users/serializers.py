from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_id','mobile','address','pincode']
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer

    class Meta:
        model = User
        fields = ['username', 'email', 'is_seller','profile']