from django.shortcuts import render,redirect, get_object_or_404
from post.models import CreatePost, Comment
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from post.forms import CommentForm
from django.urls import reverse
    
    
    
def homepage(request):
    allpost = CreatePost.objects.all().order_by('-date')
    context = {
        'allpost': allpost,
        'title':'Home',
    }
    return render(request,'home.html', context)
            

        
def Login(request):
    response_data = {}
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.POST ['username']
        password = request.POST ['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response_data = {'Login': 'success'}
    else:
        user = authenticate(username=username, password=password)
    
    return JsonResponse(response_data)


def LOGOUT (request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def signup(request):
    response_data = {}
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
    
        newuser = User.objects.create(username=username)
        newuser.set_password(password)
        newuser.save()
        response_data = {'registers': 'success'}
        return JsonResponse(response_data)
        
    return JsonResponse(response_data)


def post(request, ID):
    post = CreatePost.objects.filter( id=ID)
    postingan = get_object_or_404(CreatePost, id=ID)
    total_comments = Comment.objects.filter(id=ID).count()
    user = request.user
    
    comments = Comment.objects.filter(post=postingan).order_by("-date")
    
    
    
    if request.method == 'POST':
        is_liked = False    
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = postingan
            comment.pengguna = user
            comment.save()

        if "like" in request.POST:
            postingan.like.add(request.user)
            is_liked = True
            
        elif "dislike" in request.POST:
            postingan.like.remove(request.user)
            is_liked = False
        
        elif "delete" in request.POST:
            pk = request.POST.get('delete')
            delete_c = Comment.objects.get(pk=pk)
            delete_c.delete()
            
        return HttpResponseRedirect(reverse('post', args=[ID]), {'is_liked': is_liked})
    
    else:
        
        commentform = CommentForm()
    
    context = {
        'total_comments': total_comments,
        'commentform': commentform,
        'commentlist' : comments,
        'postingan': post,
        'title': 'Post'
    }
    return render(request, 'post.html', context)


