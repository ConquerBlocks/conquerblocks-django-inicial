family1 = Family.objects.create(
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