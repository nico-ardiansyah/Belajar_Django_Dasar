from django.db import models
from django.contrib.auth.models import User


class CreatePost(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.content