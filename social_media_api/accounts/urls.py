from django.urls import path  
from .views import UserRegisterView, LoginView, UserDetailView 
from .views import follow_user, unfollow_user


urlpatterns = [  
    path('register/', UserRegisterView.as_view(), name='user-register'),  
    path('login/', LoginView.as_view(), name='user-login'),  
    path('profile/', UserDetailView.as_view(), name='user-profile'),  
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    # Other account-related endpoints
]