from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Vistas generales de la aplicación
def course_list(request):
    return render(request, "courses/course_list.html")

def course_detail(request, id):
    return render(request, "courses/course_detail.html")

