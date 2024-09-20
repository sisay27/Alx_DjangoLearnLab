from django.db import models  
from django.contrib.auth.models import User  
from blog.models import Post

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    published_date = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Handles multiple posts by a single author

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
