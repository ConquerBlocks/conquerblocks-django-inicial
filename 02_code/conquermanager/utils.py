from todos.models import Family, Person

bienve = Person.objects.get(dni="8874746484X")

los_saez = Family.objects.create(name="Los Sáez")

family2 = Family.objects.create(name="Los Pérez")

los_saez = Family.objects.get(pk=1)
los_perez = Family.objects.get(pk=2)

p1 = Person.objects.create(
    family=family1, first_name="Bienvenido", last_name="Sáez", dni="8874746484X"
)

felipe = Person.objects.create(
    first_name="Felipe", last_name="Rodríguez", dni="887474X"
)


angela = Person.objects.create(
    family=family1, first_name="Ángela", last_name="Sáez", dni="88747464dX"
)

luis = Person.objects.create(
    family=family2, first_name="Luis", last_name="Pérez", dni="8874d4dX"
)


[family.name for family in bienve.family.all()]


for person in Person.objects.all():
    print(person)


for family in Family.objects.all():
    print(family.name)


saez = Family.objects.get(name="Los Sáez")

familias = Family.objects.all()

person_18 = Person.objects.filter(age=55)
for person in person_18:
    print(person)

person_18 = Person.objects.exclude(age=55)
for person in person_18:
    print(f"{person.first_name} - {person.age}")


# Clase 08 Crear datos

from todos.models import Family, Person
import random

# Crear 5 familias
families = []
for i in range(1, 6):
    family = Family.objects.create(name=f"Familia {i}")
    families.append(family)

# Generar datos de ejemplo para 20 personas
first_names = [
    "Juan",
    "Ana",
    "Luis",
    "María",
    "Carlos",
    "Sofía",
    "Pedro",
    "Laura",
    "Jorge",
    "Elena",
    "Miguel",
    "Lucía",
    "Pablo",
    "Carmen",
    "Andrés",
    "Paula",
    "Roberto",
    "Marta",
    "Ricardo",
    "Eva",
]
last_names = [
    "García",
    "Martínez",
    "Rodríguez",
    "López",
    "Sánchez",
    "González",
    "Pérez",
    "Hernández",
    "Díaz",
    "Torres",
    "Romero",
    "Vargas",
    "Jiménez",
    "Flores",
    "Ruiz",
    "Ortiz",
    "Morales",
    "Castro",
    "Delgado",
    "Ramos",
]

for i in range(20):
    first_name = first_names[i % len(first_names)]
    last_name = last_names[i % len(last_names)]
    age = random.randint(12, 50)
    dni = f'{random.randint(10000000, 99999999)}{random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}'

    person = Person.objects.create(
        first_name=first_name,
        last_name=last_name,
        age=age,
        dni=dni,
        family=random.choice(Family.objects.all()),
    )


# avg, sum ...
from django.db.models import Count, Avg, Sum, Min, Max
from todos.models import Person, Family

# Contar el número total de personas
total_persons = Person.objects.count()
print(f"Total de personas: {total_persons}")

# Calcular la edad promedio de las personas
average_age = Person.objects.aggregate(Avg("age"))
print(f'Edad promedio: {average_age["age__avg"]}')

# Sumar todas las edades de las personas
total_age = Person.objects.aggregate(Sum("age"))
print(f'Suma total de las edades: {total_age["age__sum"]}')

# Encontrar la edad mínima
min_age = Person.objects.aggregate(Min("age"))
print(f'Edad mínima: {min_age["age__min"]}')


# Encontrar la edad máxima
max_age = Person.objects.aggregate(Max("age"))
print(f'Edad máxima: {max_age["age__max"]}')

# Consultas de agregación agrupadas por familia

# Contar el número de personas por familia
persons_per_family = Family.objects.annotate(num_persons=Count("members"))
for family in persons_per_family:
    print(f"Familia {family.name} tiene {family.num_persons} personas")

# Calcular la edad promedio por familia
average_age_per_family = Family.objects.annotate(average_age=Avg("members__age"))
for family in average_age_per_family:
    print(f"La edad promedio en la familia {family.name} es {family.average_age}")

# Sumar las edades por familia
total_age_per_family = Family.objects.annotate(total_age=Sum("members__age"))
for family in total_age_per_family:
    print(
        f"La suma total de las edades en la familia {family.name} es {family.total_age}"
    )

# Encontrar la edad mínima por familia
min_age_per_family = Family.objects.annotate(min_age=Min("members__age"))
for family in min_age_per_family:
    print(f"La edad mínima en la familia {family.name} es {family.min_age}")

# Encontrar la edad máxima por familia
max_age_per_family = Family.objects.annotate(max_age=Max("members__age"))
for family in max_age_per_family:
    print(f"La edad máxima en la familia {family.name} es {family.max_age}")


# Manager para personas adultas
from django.db import models


class PersonManager(models.Manager):
    def adults(self):
        return self.filter(age__gt=18)


class Family(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"


class Person(models.Model):
    family = models.ManyToManyField(Family)

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


# Consultar personas mayores de 18 años
adult_persons = Person.objects.adults()
for person in adult_persons:
    print(person)


# Q con OR
from django.db.models import Q
from todos.models import Person

# Filtrar personas que se llamen 'Juan' o que sean mayores de 18 años
results_or = Person.objects.filter(Q(first_name="Juan") | Q(age__gt=18))

for person in results_or:
    print(person)


# Q con AND
from django.db.models import Q
from myapp.models import Person

# Filtrar personas que se llamen 'Juan' y que sean mayores de 18 años
results_and = Person.objects.filter(Q(first_name="Juan") & Q(age__gt=18))

for person in results_and:
    print(person)


# Ejemplo combinando Q Objects con AND y OR: Finalmente, si quieres hacer una consulta más compleja que involucre tanto AND como OR, por ejemplo, encontrar todas las personas que se llamen ‘Juan’ y que sean mayores de 18 años, o que tengan un apellido específico.
from django.db.models import Q
from todos.models import Person

# Filtrar personas que se llamen 'Juan' y sean mayores de 18 años, o que tengan el apellido 'García'
complex_query = Person.objects.filter(
    (Q(first_name="Juan") & Q(age__gt=18)) | Q(last_name="García")
)

for person in complex_query:
    print(person)

# Clase de teoría de mates y conjuntos


# Select related
from django.db import models


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


# Ejemplo de select related
from todos.models import Person

# Consultar personas y sus familias usando select_related
persons_with_families = Person.objects.select_related("family").all()

for person in persons_with_families:
    print(
        f"{person.first_name} {person.last_name} pertenece a la familia {person.family.name}"
    )


# Consulta usando prefetch_related para relaciones ManyToMany
persons_with_families = Person.objects.prefetch_related("family").all()

for person in persons_with_families:
    family_names = ", ".join(family.name for family in person.family.all())
    print(
        f"{person.first_name} {person.last_name} pertenece a las familias {family_names}"
    )
