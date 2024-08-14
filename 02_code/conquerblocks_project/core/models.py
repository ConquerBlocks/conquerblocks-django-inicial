from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=50
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    comentario = models.TextField(
        verbose_name='Comentario que ha dejado en la web'
    )
    created_at = models.DateTimeField(
        verbose_name='Fecha y hora de creación',
        default=timezone.now
    )
    contactado = models.BooleanField(
        verbose_name='¿Se ha contactado con él?',
        default=False
    )

    def __str__(self):
        return self.nombre