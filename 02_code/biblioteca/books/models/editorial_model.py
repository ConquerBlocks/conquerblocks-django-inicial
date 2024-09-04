from django.db import models
from django.contrib.auth.models import User


# Modelo para Editoriales
class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    sitio_web = models.URLField(null=True, blank=True)
    fecha_fundacion = models.DateField()
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre
