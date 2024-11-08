from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.userlogin, name='login'),
    path('user/', include('User.urls')),
    path('post/', include('post.urls')),
    # path('user/', include('User.urls')),
    # path('post/', include('post.urls')),
]
