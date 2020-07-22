from django.shortcuts import render
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})