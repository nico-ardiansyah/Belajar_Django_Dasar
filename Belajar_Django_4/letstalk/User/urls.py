from django.urls import path 
from . import views

app_name = 'USER'

urlpatterns = [
    path('', views.userpage, name='profile'),
    
]
