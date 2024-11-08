from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages




# Create your views here.
APP_NAME = 'user'


def userpage(request):
    context = {
        'title' : 'Profile'
    }
    return render(request, f'{APP_NAME}/userpage.html', context)
    
def register(request):
    if request.method == 'POST':
        createUser = UserCreationForm(request.POST)
        if createUser.is_valid():
            createUser.save()
            return redirect('login')
        
    else:
        
        createUser = UserCreationForm()
        
        
    context = {
        'title': 'Registration',
        'createUser': createUser,
    }
    return render(request, 'user/register.html', context)
    
def LOGOUT (request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
