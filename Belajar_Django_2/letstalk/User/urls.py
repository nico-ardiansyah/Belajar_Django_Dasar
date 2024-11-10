from django.urls import path 
from . import views

app_name = 'USER'

urlpatterns = [
    path('', views.userpage, name='profile'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.LOGOUT, name='logout'),
    
]