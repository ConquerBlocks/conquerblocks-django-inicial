# Nuestra primera vista

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

# Conectemos nuestra vista

# Creemos nuestra primera url
# Importamos nuestra vista y la conectamos con una url

# Definir donde están nuestras plantillas
TEMPLATES_DIR = BASE_DIR / "biblioteca" / "templates"

# Crear urls para Inicio

# Crear url y vista para autores

# Crear urls y vista para libros

# Crear urls y vista para editorial

# Crear urls y vista para contacto

# Definamos datos a mano
autores = [
  {"nombre": "Antonio"},
  {"nombre": "Juan"},
]

context = {
  "autores": autores,
}

return render(request, 'autores.html', context)

# Pasemos datos al template


# Organización de urls por aplicación
# Crear fichero de urls por aplicación
# Partes de una url string, vista y nombre
# Qué recibe una vista

def home_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    print(request)
    return render(request, 'home.html')

# Qué trae el request request.__dict__

path("", home_view, name="home"),
path("autores/<int:id>", autores_list)
path("lisbros/editorial/<str:editorial>", autores_list)
