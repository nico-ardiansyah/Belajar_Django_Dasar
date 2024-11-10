from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from post.models import CreatePost



# Create your views here.
APP_NAME = 'user'


def userpage(request):
    post = CreatePost.objects.filter(author=request.user)
    context = {
        'post': post,
        'title' : 'Profile'
    }
    return render(request, 'user/userpage.html', context)
    
def register(request):
    if request.method == 'POST':
        createUser = UserCreationForm(request.POST)
        if createUser.is_valid():
            createUser.save()
            return redirect('USER:login')
        
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
    
    
def userlogin(request):
    if request.method == "POST":
        userlogin = AuthenticationForm(data=request.POST)
        if userlogin.is_valid():
            login(request, userlogin.get_user())
            return redirect('home')
    else:
        userlogin = AuthenticationForm()
    
    context = {
        'title':'login',
        'userlogin': userlogin,
    }
    
    return render(request,'user/loginuser.html', context)


