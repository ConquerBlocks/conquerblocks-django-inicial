from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Post

# Vistas generales de la aplicación
def blog_list(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, "blog/blog_list.html", context)

def blog_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, "blog/blog_detail.html", context)

