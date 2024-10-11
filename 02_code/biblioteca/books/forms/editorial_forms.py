from django import forms
from django.forms import ModelForm
from books.models import Editorial
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=300, required=False)
    ciudad = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    fecha_fundacion = forms.DateField(widget = forms.SelectDateWidget)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre


class EditorialModelFormCreate(ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'nombre',
            'direccion',
            'email',
            'fecha_fundacion',
            'level',
            'sitio_web'
        ]

