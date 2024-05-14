from rest_framework import serializers
from .models import CustomUser, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["mobile", "address", "pincode"]

        def validate_pincode(self, value):
         expected_length = 5  
         if len(value) != expected_length:
            raise  serializers.ValidationError(f"The pincode must be exactly {expected_length} characters long.")
         return value

    def validate_mobile(self, value):
        expected_length = 10  
        if len(value) != expected_length:
            raise serializers.ValidationError(f"The mobile number must be exactly {expected_length} characters long.")
        return value


class BuyerSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}
        def validate_password(self, value):
         min_length = 8  
         if len(value) < min_length:
            raise serializers.ValidationError(f"The password must be at least {min_length} characters long.")
         return value

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", {})  
        password = validated_data.pop("password") 
        user = CustomUser.objects.create_user(**validated_data)  
        user.set_password(password) 
        user.save()  
        Profile.objects.create(user=user, **profile_data)  
        return user  
        



    

class BuyerSigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CustomUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile',{})
        profile_serializer = self.fields['profile']
        profile_instance = instance.profile

        for attr, value in profile_data.items():
            setattr(profile_instance, attr, value)

        profile_instance.save()

        return super().update(instance, validated_data)

