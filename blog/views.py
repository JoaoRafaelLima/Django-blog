from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    current_post = Post.objects.last()
    return render(request, "posts/home.html", {"current_post": current_post})

def dashboard(request):
    return render(request, "posts/dashboard.html")

def editor(request, id_or_new):

    if request.method == "POST":
        if id_or_new == "new":
            form = PostForm(request.POST)
            post = form.save()
        else:
            idp = int(id_or_new)
            post = get_object_or_404(Post, pk=idp)
            post_update = PostForm(request.POST, instance=post)
            post_update.save()

        return redirect("/")
    else:
        if id_or_new == "new":
            formGet = PostForm()
            formGet.title = " "
            formGet.content = " "
            
        else: 
            idp = int(id_or_new)
            post = get_object_or_404(Post, pk=idp)
            formGet = PostForm(instance=post)

        return render(request, "posts/editor.html", { "form": formGet, "arg": id_or_new})


def  read_post(request, idp):
    current_post = Post.objects.filter(id=idp)[0]
    return render(request, "posts/home.html", {"current_post": current_post})

def list_posts(request):
    search = request.GET.get("search")
  
    if search:
        is_search = search
        posts_list = Post.objects.filter(title__icontains=search)
    else:
        is_search = None
        posts_list = Post.objects.values('title', 'id').order_by("-created_at")
        
            
    
    paginator = Paginator(posts_list, 6)
    try:
        #page = int(request.GET.get('page', '1'))
        page = request.GET.get("page")
    except ValueError:
        page = 1
    posts = paginator.get_page(page)
    return render(
        request, "posts/posts.html",
        {"posts_list": posts, "is_search": is_search}
        )