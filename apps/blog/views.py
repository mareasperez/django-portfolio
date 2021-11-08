from django.shortcuts import render, get_object_or_404
from .models import Post


def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_by_id(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})
