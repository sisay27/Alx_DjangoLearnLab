from rest_framework import generics, permissions  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from .serializers import UserRegisterSerializer, UserSerializer, TokenSerializer  
from django.contrib.auth import get_user_model  

User = get_user_model()  

class UserRegisterView(generics.CreateAPIView):  
    queryset = User.objects.all()  
    serializer_class = UserRegisterSerializer  
    permission_classes = [permissions.AllowAny]  

class LoginView(ObtainAuthToken):  
    def post(self, request, *args, **kwargs):  
        serializer = self.serializer_class(data=request.data)  
        serializer.is_valid(raise_exception=True)  
        user = serializer.validated_data['user']  
        token, created = Token.objects.get_or_create(user=user)  
        return Response({'token': token.key})  

class UserDetailView(generics.RetrieveUpdateAPIView):  
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    permission_classes = [permissions.IsAuthenticated]