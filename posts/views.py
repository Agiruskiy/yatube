from django.shortcuts import render
from .models import Post
# Create your views here.

def first(request):
    post = Post.objects.all()
    return render(request, './index.html', {
        'post' : post
    })