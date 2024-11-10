from django.shortcuts import render,redirect
from post.models import CreatePost
    
def homepage(request):
    allpost = CreatePost.objects.all().order_by('-date')
    context = {
        'allpost': allpost,
        'title':'Home',
    }
    return render(request,'home.html', context)
            
    