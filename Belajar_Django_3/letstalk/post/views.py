from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def Create_Post(request):
    if request.method == 'POST':
        CreatePost = forms.NewPost(request.POST, request.FILES)
        if CreatePost.is_valid():
            newpost = CreatePost.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('home')
            
    else:
        CreatePost = forms.NewPost()
    return render(request, 'post/createpost.html', {'CreatePost': CreatePost})