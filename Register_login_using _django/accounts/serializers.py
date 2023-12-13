from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Add more fields if needed
        # extra_kwargs = {'password': {'write_only': True}}

#Register Setializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','password']  # Add more fields if needed
        extra_kwargs = {'password': {'write_only': True}}


        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])

            return user