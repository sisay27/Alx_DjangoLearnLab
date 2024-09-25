from django.urls import path  
from .views import UserRegisterView, LoginView, UserDetailView  

urlpatterns = [  
    path('register/', UserRegisterView.as_view(), name='user-register'),  
    path('login/', LoginView.as_view(), name='user-login'),  
    path('profile/', UserDetailView.as_view(), name='user-profile'),  
]