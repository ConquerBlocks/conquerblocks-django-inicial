from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Vistas generales de la aplicación
def home(request):
    return render(request, "core/home.html")

def about_us(request):
    return render(request, "core/about_us.html")

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")

def contact(request):
    return render(request, "core/contact.html")
