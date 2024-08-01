from django.shortcuts import render


def editoriales_view(request):
    return render(request, "editoriales/editoriales.html")
