from django.contrib import admin
from .models import CreatePost, Comment


# Register your models here.
admin.site.register(CreatePost)
admin.site.register(Comment)