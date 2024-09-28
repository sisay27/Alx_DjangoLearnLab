from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like = Like(post=post, user=user)
    like.save()

    # Create a notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked your post',
        target=post
    )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user

class PostPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        followed_posts = Post.objects.filter(author__in=following_users)
        return followed_posts.order_by('-created_at')
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like = Like(post=post, user=user)
    like.save()

    # Create a notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked your post',
        target=post
    )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)