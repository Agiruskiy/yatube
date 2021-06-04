from django.shortcuts import render
from .models import Post
# Create your views here.

def first(request):
    post = Post.objects.order_by("-pub_date")[:11]
    return render(request, 'index.html', {
        'post' : post
    })