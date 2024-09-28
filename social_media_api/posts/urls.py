from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FeedView
from .views import like_post


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    # Add other URLs as needed
]