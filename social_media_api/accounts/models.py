from django.db import models  
from django.contrib.auth.models import AbstractUser  

class CustomUser(AbstractUser):  
    bio = models.TextField(blank=True, null=True)  
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)  

# Reminder: Don't forget to set AUTH_USER_MODEL in settings.py