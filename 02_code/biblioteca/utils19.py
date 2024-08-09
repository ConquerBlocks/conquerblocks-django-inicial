from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar')


# ====

from django.shortcuts import render
from .forms import SearchForm
from .models import Contact

def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        # Filtrar los contactos por nombre o email que contengan la consulta
        results = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(email__icontains=query)

    return render(request, 'search.html', {'form': form, 'results': results})


# ====

# <!DOCTYPE html>
# <html>
# <head>
#     <title>Search Contacts</title>
# </head>
# <body>
#     <h1>Buscar Contactos</h1>
#     <form method="get">
#         {{ form.as_p }}
#         <button type="submit">Buscar</button>
#     </form>

#     <h2>Resultados</h2>
#     <ul>
#         {% for contact in results %}
#             <li>{{ contact.name }} - {{ contact.email }}</li>
#         {% empty %}
#             <li>No se encontraron resultados.</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>


# ====


# Ahora hagamos ese desplegable relleno con un choices


from django import forms
from .models import Category


class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('friends', 'Amigos'),
        ('family', 'Familia'),
        ('work', 'Trabajo'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.shortcuts import render
from .forms import ContactSearchForm
from .models import Contact

def contact_filter_view(request):
    form = ContactSearchForm(request.GET)
    results = []

    if form.is_valid():
        category = form.cleaned_data['category']
        # Filtrar los contactos por categoría seleccionada
        results = Contact.objects.filter(category=category)

    return render(request, 'contact_filter.html', {'form': form, 'results': results})




class ContactSearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Categoría',
        empty_label='Seleccione una categoría'
    )



from django.shortcuts import render
from .forms import ContactSearchForm
from .models import Contact

def contact_filter_view(request):
    form = ContactSearchForm(request.GET)
    results = []

    if form.is_valid():
        category = form.cleaned_data['category']
        # Filtrar los contactos por la categoría seleccionada
        results = Contact.objects.filter(category=category)

    return render(request, 'contact_filter.html', {'form': form, 'results': results})




from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ====


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo Electrónico')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if "spam" in email:
    #         raise forms.ValidationError("El correo electrónico no puede contener la palabra 'spam'.")
    #     return email

# ====


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Crear una instancia del modelo Contact sin guardarla inmediatamente
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # Guardar la instancia en la base de datos
            contact.save()

            # Redirigir a una página de agradecimiento
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# ====



# <!DOCTYPE html>
# <html>
# <head>
#     <title>Contact Us</title>
# </head>
# <body>
#     <h1>Contáctanos</h1>
#     <form method="post">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Enviar</button>
#     </form>
# </body>
# </html>
