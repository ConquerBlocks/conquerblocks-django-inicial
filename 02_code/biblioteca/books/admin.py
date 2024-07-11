from django.contrib import admin

from books.models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'fecha_nacimiento')
        export_order = ('nombre', 'apellido', 'fecha_nacimiento')


class LibroInline(admin.StackedInline):
    model = Libro

@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource
    list_display = [
       "pk", "nombre", "apellido", "fecha_nacimiento", "email", "telefono"
    ]
    ordering = ["apellido", "nombre", ]



@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = [
       "nombre", "ciudad", "telefono", "email", "sitio_web", "fecha_fundacion"
    ]
    list_filter = ["fecha_fundacion"]
    inlines = [
        LibroInline,
    ]


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
       "titulo", "editorial", "isbn", "fecha_publicacion", "numero_paginas", "idioma", 
    ]
    list_filter = ["editorial", "idioma"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ('autores', )



