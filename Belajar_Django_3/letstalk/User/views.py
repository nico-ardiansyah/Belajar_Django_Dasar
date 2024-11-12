from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from post.models import CreatePost
from post import forms


# Create your views here.
APP_NAME = 'user'


def userpage(request):
    post = CreatePost.objects.filter(author=request.user).order_by('-date')
    UpdateForm = CreatePost.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            pk = request.POST.get('delete')
            postingan = CreatePost.objects.get(id=pk)
            postingan.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            postingan = CreatePost.objects.get(id=pk)
            UpdateForm = forms.NewPost(instance=postingan)
        elif 'save' in request.POST:
            pk = request.POST.get('save')
            postingan = CreatePost.objects.get(id=pk)
            UpdateForm = forms.NewPost(request.POST, request.FILES or None, instance=postingan)
            if UpdateForm.is_valid():
                UpdateForm.save()
                return redirect ('USER:profile')
            UpdateForm = CreatePost()
        else:
            UpdateForm =forms. NewPost(request.FILES or None, instance=postingan)
    context = {
        'UpdateForm': UpdateForm,
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


