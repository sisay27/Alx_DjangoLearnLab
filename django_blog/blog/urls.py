from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    # Other existing URL patterns for your blog app
    
    # URL pattern for adding a new comment
    path('posts/<int:post_id>/comments/new/', views.post_detail, name='add_comment'),

    # URL pattern for editing a comment
    path('comments/<int:comment_id>/edit/', views.comment_edit, name='edit_comment'),

    # URL pattern for deleting a comment
    path('comments/<int:comment_id>/delete/', views.comment_delete, name='delete_comment'),
    # Other URL patterns
    
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='new_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]