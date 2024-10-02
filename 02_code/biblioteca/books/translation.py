from modeltranslation.translator import translator, TranslationOptions
from .models import Libro

class LibroTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion')

translator.register(Libro, LibroTranslationOptions)