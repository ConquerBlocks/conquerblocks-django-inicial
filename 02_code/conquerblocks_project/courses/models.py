from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    title = models.CharField(
        verbose_name='Título del curso',
        max_length=200
    )
    content = models.TextField(
        verbose_name='Contenido del curso',
    )
    call_link = models.URLField(
        verbose_name='Enlace de llamada'
    )
    created_at = models.DateTimeField(
        verbose_name='Fecha y hora de creación',
        default=timezone.now
    )

    def __str__(self):
        return self.title