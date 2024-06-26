from django.db import models

class Family(models.Model):
    name = models.CharField(
        max_length=140,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"


class Person(models.Model):
    family = models.ManyToManyField(
        Family
    )

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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ["age"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
