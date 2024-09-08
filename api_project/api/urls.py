# api_project/urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls