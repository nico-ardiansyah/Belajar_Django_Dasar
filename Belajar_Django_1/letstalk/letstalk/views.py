from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
    

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
    
    return render(request, 'loginuser.html', context)


def homepage(request):
    context = {
        'title':'Home',
    }
    return render(request, 'home.html' , context)
            
    