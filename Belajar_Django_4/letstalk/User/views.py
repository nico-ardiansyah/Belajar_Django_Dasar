from django.shortcuts import render, redirect
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
    


