from django.db import models


class PersonManager(models.Manager):
    def adults(self):
        return self.filter(age__gte=18)

    def childs(self):
        return self.filter(age__lt=18)


class Family(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"


class Person(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="members")

    first_name = models.CharField("Nombre", max_length=30)

    last_name = models.CharField("Apellidos", max_length=30)

    age = models.IntegerField(
        "Edad", default=18, help_text="Introduce tu edad en formato número"
    )
    dni = models.CharField("DNI", max_length=9, unique=True)

    objects = PersonManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["age"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
