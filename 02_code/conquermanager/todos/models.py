from django.db import models

class Person(models.Model):
    first_name = models.CharField(
        'Nombre',
        max_length=30
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=30
    )
    age = models.IntegerField(
        'Edad',
        default=18,
        help_text='Introduce tu edad en formato número'
    )
    dni = models.CharField(
        'DNI',
        max_length=9,
        unique=True
    )
