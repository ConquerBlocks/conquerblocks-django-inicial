from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from courses.models import Course
from blog.models import Post

# Vistas generales de la aplicación
def home(request):
    
    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True)
    }
    return render(request, "core/home.html", context)

def about_us(request):
    return render(request, "core/about_us.html")

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")

def contact(request):
    return render(request, "core/contact.html")
