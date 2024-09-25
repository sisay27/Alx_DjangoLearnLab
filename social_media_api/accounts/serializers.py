# accounts/serializers.py  

from rest_framework import serializers  
from django.contrib.auth import get_user_model  
from django.contrib.auth.models import User  
from rest_framework.authtoken.models import Token  

class UserRegisterSerializer(serializers.ModelSerializer):  
    # Define fields, including CharField for username and password  
    username = serializers.CharField(max_length=150)  
    password = serializers.CharField(write_only=True)  

    class Meta:  
        model = User  
        fields = ('username', 'password', 'bio', 'profile_picture')  

    def create(self, validated_data):  
        # Create the user using the create_user method  
        user = get_user_model().objects.create_user(  
            username=validated_data['username'],  
            password=validated_data['password'],  
            # Include other fields here if necessary  
        )  
        user.bio = validated_data.get('bio', '')  
        user.profile_picture = validated_data.get('profile_picture', None)  
        user.save()  

        # Create a token for the user after registration  
        Token.objects.create(user=user)  

        return user  


class LoginSerializer(serializers.Serializer):  
    username = serializers.CharField(required=True, max_length=150)  
    password = serializers.CharField(required=True)  

    def validate(self, attrs):  
        user = get_user_model().objects.filter(username=attrs['username']).first()  
        if user is None:  
            raise serializers.ValidationError("User with this username does not exist.")  
        if not user.check_password(attrs['password']):  
            raise serializers.ValidationError("Incorrect password.")  

        attrs['user'] = user  
        attrs['token'] = Token.objects.get(user=user).key  
        return attrs  


class UserDetailSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ('username', 'bio', 'profile_picture')  

    def update(self, instance, validated_data):  
        instance.bio = validated_data.get('bio', instance.bio)  
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)  
        instance.save()  
        return instance