from rest_framework import generics, permissions  
from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response  
from .serializers import UserRegisterSerializer, UserSerializer, TokenSerializer  
from django.contrib.auth import get_user_model  
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = CustomUser.objects.get(id=user_id)
    
    if request.user == user_to_follow:
        return Response("You cannot follow yourself.", status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    return Response("Successfully followed user.", status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = CustomUser.objects.get(id=user_id)
    
    if user_to_unfollow in request.user.following.all():
        request.user.following.remove(user_to_unfollow)
        return Response("Successfully unfollowed user.", status=status.HTTP_200_OK)
    else:
        return Response("User is not in your following list.", status=status.HTTP_400_BAD_REQUEST)