from django.conf import settings

def get_clave(request):
  return {
    'CLAVE' : settings.CLAVE,
    'COLOR': settings.COLOR
  }