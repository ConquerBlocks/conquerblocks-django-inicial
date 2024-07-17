from django.shortcuts import render

def autores_view(request):
    autores = [
      {
          "id": 1,
          "nombre": "Antonio"
      },
      {
          "id": 2,
          "nombre": "Felipe"
      },
      {
          "id": 3,
          "nombre": "Matilde"
      },
    ]

    context = {
        "autores": autores,
        "titulo": "Hola esto es otra prueba de paso de contexto"
    }

    return render(request, 'autores/autores.html', context)


def autor_detail(request, id):

    autores = [
      {
          "id": 1,
          "nombre": "Antonio"
      },
      {
          "id": 2,
          "nombre": "Felipe"
      },
      {
          "id": 3,
          "nombre": "Matilde"
      },
    ]

    context = {
        "autor": None,
    }
    for autor in autores:
        if autor['id'] == id:
            context['autor'] = autor

    return render(request, 'autores/autor_detail.html', context)
