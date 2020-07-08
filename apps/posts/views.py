from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def home(request):
    current_post = Post.objects.all().order_by('-created_at')[0]
    return render(request, "posts/home.html", {"current_post": current_post})

def  read_post(request, idp):
    current_post = Post.objects.filter(id=idp)[0]
    return render(request, "posts/home.html", {"current_post": current_post})

def list_posts(request):
    posts_list = Post.objects.values('title', 'id').order_by("-created_at")
    paginator = Paginator(posts_list, 3)
    try:
        #page = int(request.GET.get('page', '1'))
        page = request.GET.get("page")
    except ValueError:
        page = 1
    posts = paginator.get_page(page)
    return render(request, "posts/posts.html", {"posts_list": posts})