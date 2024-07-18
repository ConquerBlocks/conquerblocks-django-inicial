from django.shortcuts import render

# Vistas generales de la aplicación
def home_view(request):
    return render(request, 'general/home.html')

def contact_view(request):
    return render(request, 'general/contacto.html')