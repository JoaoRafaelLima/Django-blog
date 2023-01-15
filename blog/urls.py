from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.list_posts, name="list-posts"),
    path('post/<int:idp>', views.read_post, name="post"),
    path('editor/<str:id_or_new>', views.editor, name="new-post"),
    path('dashboard/', views.dashboard, name="dash"),
]