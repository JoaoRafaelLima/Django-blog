from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    current_post = Post.objects.all().order_by('-created_at')[0]
    return render(request, "posts/home.html", {"current_post": current_post})

def  read_post(request, idp):
    current_post = Post.objects.filter(id=idp)[0]
    return render(request, "posts/home.html", {"current_post": current_post})

def list_posts(request):
    posts_title = Post.objects.values('title', 'id')
    return render(request, "posts/posts.html", {"posts_list": posts_title})