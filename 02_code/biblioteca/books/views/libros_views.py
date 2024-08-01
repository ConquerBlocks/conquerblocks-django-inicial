from django.shortcuts import render


def libros_view(request):
    return render(request, "libros/libros.html")
