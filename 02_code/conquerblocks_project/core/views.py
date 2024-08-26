from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.shortcuts import render
from django.views.generic.edit import FormView

from courses.models import Course
from blog.models import Post
from .forms import ContactForm, LoginForm, UserRegisterForm
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


# Vistas generales de la aplicación
def home(request):
    context = {
        'courses': Course.objects.filter(show_home=True),
        'posts': Post.objects.filter(show_home=True)
    }
    return render(request, "core/home.html", context)

def about_us(request):
    return render(request, "core/about_us.html")

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
            else:
                context = {
                  'form': form,
                  'error': True,
                  'error_message': 'Usuario no válido' 
                }
                return render(request, "core/login.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "core/login.html", context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, "core/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))

def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            user = User.objects.create_user(username, email, password2)
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            context = {
                'msj': 'Usuario creado correctamente'
            }

            return render(request, "core/register.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "core/register.html", context)
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, "core/login.html", context)



    return render(request, "core/register.html")

def contact(request):
    if request.POST:
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']

            message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

            Contact.objects.create(
                nombre=nombre,
                email=email,
                comentario=comentario
            )

            success = send_mail(
                "Formulario de contacto de mi Web",
                message_content,
                "info@laveladaconquer.com",
                ["bienvenidosaez@gmail.com"],
                fail_silently=False,
            )

            context = {
              'form' : formulario,
              'success' : success
            }
            return render(request, "core/contact.html", context)
        else:
            context = {
              'form' : formulario,
            }
            return render(request, "core/contact.html", context)
  
    formulario = ContactForm()
    context = {
      'form' : formulario
    }
    return render(request, "core/contact.html", context)


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        comentario = form.cleaned_data['comentario']

        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

        Contact.objects.create(
            nombre=nombre,
            email=email,
            comentario=comentario
        )

        success = send_mail(
            "Formulario de contacto de mi Web",
            message_content,
            "info@laveladaconquer.com",
            ["bienvenidosaez@gmail.com"],
            fail_silently=False,
        )

        return super().form_valid(form)

class Prueba(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")

class PruebaTemplateView(TemplateView):
    template_name = "PruebaTemplateView.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Este es mi título'
        return context
