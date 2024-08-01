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
