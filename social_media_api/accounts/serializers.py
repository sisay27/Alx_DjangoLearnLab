# accounts/serializers.py  

from rest_framework import serializers  
from django.contrib.auth import get_user_model  
from django.contrib.auth.models import User  
from rest_framework.authtoken.models import Token  

class UserRegisterSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ('username', 'password', 'bio', 'profile_picture')  
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):  
        user = get_user_model()(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        Token.objects.create(user=user)  
        return user  


class LoginSerializer(serializers.Serializer):  
    username = serializers.CharField(required=True)  
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