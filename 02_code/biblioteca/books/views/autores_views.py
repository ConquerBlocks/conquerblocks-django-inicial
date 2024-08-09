from django.shortcuts import render
from datetime import date

from books.models import Autor


def autores_view(request):
    autores = Autor.objects.all()

    context = {
        "autores": autores,
        "titulo": "Hola esto es otra prueba de paso de contexto",
    }

    return render(request, "autores/autores.html", context)


def autor_detail(request, id):

    autores = [
        {"id": 1, "nombre": "Antonio", "f_nac": date(1980, 8, 1)},
        {"id": 2, "nombre": "Felipe", "f_nac": date(1985, 10, 1)},
        {"id": 3, "nombre": "Matilde", "f_nac": date(1990, 11, 5)},
    ]

    context = {
        "autor": None,
    }
    for autor in autores:
        if autor["id"] == id:
            context["autor"] = autor
            break

    return render(request, "autores/autor_detail.html", context)
