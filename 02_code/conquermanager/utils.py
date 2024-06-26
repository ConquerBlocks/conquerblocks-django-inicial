from todos.models import Family, Person

bienve = Person.objects.get(dni='8874746484X')

los_saez = Family.objects.create(
  name="Los Sáez"
)

family2 = Family.objects.create(
  name="Los Pérez"
)

los_saez = Family.objects.get(pk=1)
los_perez = Family.objects.get(pk=2)

p1 = Person.objects.create(
  family=family1,
  first_name='Bienvenido',
  last_name='Sáez',
  dni='8874746484X'
)

felipe = Person.objects.create(
  first_name='Felipe',
  last_name='Rodríguez',
  dni='887474X'
)


angela = Person.objects.create(
  family=family1,
  first_name='Ángela',
  last_name='Sáez',
  dni='88747464dX'
)

luis = Person.objects.create(
  family=family2,
  first_name='Luis',
  last_name='Pérez',
  dni='8874d4dX'
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
    print(f'{person.first_name} - {person.age}')

