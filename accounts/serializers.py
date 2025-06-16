from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in API responses

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Required fields for registration

    def create(self, validated_data):
        user = User.objects.create_user(  # Creates user with hashed password
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Required field for login
    password = serializers.CharField(write_only=True,style={'input_type': 'password','autocomplete':'new-password'})  # Do not expose password in responses

    def validate(self, data):
        user = authenticate(**data)  # Authentiactes user credentials
        if user and user.is_active:
            return user  # Valid and active user
        raise serializers.ValidationError("Wrong Credentials")  # Raise error on failed login
