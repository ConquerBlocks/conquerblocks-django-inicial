from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .forms import RegistrationForm, LoginForm


class HomeView(TemplateView):
    template_name = "general/home.html"


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)

        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.add_message(
                self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
            return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente.")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_name = "general/legal.html"


class ContactView(TemplateView):
    template_name = "general/contact.html"


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente.")
    return HttpResponseRedirect(reverse('home'))
