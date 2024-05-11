from django.shortcuts import render
from .models import Post, Author

def home(request): 
    posts = Post.objects.filter(first_line_news=True)
    return render(request, 'home.html', {'posts': posts})

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'post.html', {'post': post})
    except:
        return render(request, '404.html')

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all_posts.html', {'posts': posts})

