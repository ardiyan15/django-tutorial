from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post_id__id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment})