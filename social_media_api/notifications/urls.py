# notifications/urls.py
from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    # Add other URLs as needed
]