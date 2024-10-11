from typing import Any
from django.shortcuts import render
from books.forms import EditorialCreate, EditorialModelFormCreate
from books.models import Editorial
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from books.decorators import user_can_delete_editorial

class EditorialListView(ListView):
    model = Editorial
    template_name = "editoriales/EditorialList.html"
    context_object_name = 'editoriales'


class EditorialDetailView(DetailView):
    model = Editorial
    template_name = "editoriales/EditorialDetail.html"
    context_object_name = 'editorial'


@method_decorator(login_required, name="dispatch")
class EditorialCreateView(CreateView):
    model = Editorial
    template_name = "editoriales/EditorialCreate.html"
    success_url = reverse_lazy('editorial:list')
    form_class = EditorialModelFormCreate

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialUpdateView(UpdateView):
    model = Editorial
    template_name = "editoriales/EditorialUpdate.html"
    success_url = reverse_lazy('editorial:list')
    fields = [
        'nombre', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal','telefono', 'email', 'sitio_web', 'fecha_fundacion'
    ]

@method_decorator(user_can_delete_editorial, name="dispatch")
class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = "editoriales/EditorialDelete.html"
    success_url = reverse_lazy('editorial:list')

