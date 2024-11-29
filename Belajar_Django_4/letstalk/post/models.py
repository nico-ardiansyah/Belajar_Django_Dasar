from django.db import models
from django.contrib.auth.models import User


class CreatePost(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.FileField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    like = models.ManyToManyField(User, blank=True, related_name="like")
    def __str__(self):
        return self.content
    
    
class Comment(models.Model):
    post = models.ForeignKey(CreatePost, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    
    def __str__(self) :
        return self.comment_text
    
    
    