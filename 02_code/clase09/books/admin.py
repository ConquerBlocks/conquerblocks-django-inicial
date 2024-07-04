from django.contrib import admin

from books.models import Autor, Editorial, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
   pass


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
   pass



@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
   pass