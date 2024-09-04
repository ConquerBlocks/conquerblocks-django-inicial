# Email con Gmail





# Created by
from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo



from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Libro

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'fecha_publicacion']
    template_name = 'libro_form.html'
    success_url = reverse_lazy('libro-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.created_by = request.user
            libro.save()
            return redirect('libro-list')
    else:
        form = LibroForm()

    return render(request, 'libro_form.html', {'form': form})

# decorators.py

from django.utils.decorators import method_decorator
from functools import wraps
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.http import Http404

from ithaka.users.models import User

from ithaka.installations.models import Installation


# def es_administrador(usuario):
#     return usuario.is_superuser or usuario.groups.filter(name='admin').exists()

class is_global_user(object):

    def __init__(self, view_func):
        self.view_func = view_func
        wraps(view_func)(self)

    def __call__(self, request, *args, **kwargs):
        response = self.view_func(request, *args, **kwargs)
        if request.user and (request.user.is_eveon_user or request.user.is_superuser):
            return response
        raise PermissionDenied



def user_can_view_installation(function):
    def wrap(request, *args, **kwargs):
        try:
            installation = Installation.objects.get(pk=kwargs["pk"])
        except Installation.DoesNotExist:
            raise Http404

        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        elif request.user.is_global_user and request.user in installation.users_to_notify.all():
            return function(request, *args, **kwargs)

        raise PermissionDenied

    return wrap



# Middleware
import time

class TiempoDeProcesamientoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código que se ejecuta antes de que la vista sea llamada
        tiempo_inicio = time.time()

        response = self.get_response(request)

        # Código que se ejecuta después de que la vista ha sido llamada
        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio

        # Añadir el tiempo de procesamiento a la respuesta como una cabecera HTTP
        response['X-Tiempo-De-Procesamiento'] = str(tiempo_total)

        return response


MIDDLEWARE = [
    # Otros middlewares...
    'mi_aplicacion.middleware.TiempoDeProcesamientoMiddleware',
]


# Otro ejemplo

from django.shortcuts import render
from datetime import datetime

def mi_vista(request):
    hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'mi_template.html', {'hora_actual': hora_actual})



# Usando el middleware

from datetime import datetime

class HoraSistemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Procesar la solicitud antes de que llegue a la vista
        response = self.get_response(request)

        # Obtener la hora actual del sistema
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Añadir la hora a la respuesta como una cabecera HTTP
        response['X-Hora-Del-Sistema'] = hora_actual

        return response


<p>La hora del sistema es: {{ request.META['HTTP_X_HORA_DEL_SISTEMA'] }}</p>
