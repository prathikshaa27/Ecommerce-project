from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['mobile', 'address', 'pincode']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_seller', 'profile']
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password')  
        user = User.objects.create_user(**validated_data)
        user.set_password(password) 
        user.save()

        Profile.objects.create(user=user, **profile_data)
        return user
