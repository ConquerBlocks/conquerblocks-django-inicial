from django.contrib import admin

from books.models import Autor, Editorial, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        fields = ("nombre", "apellido", "fecha_nacimiento")
        export_order = ("nombre", "apellido", "fecha_nacimiento")


class LibroInline(admin.StackedInline):
    model = Libro


@admin.register(Autor)
class AutorAdmin(ImportExportModelAdmin):
    resource_class = AutorResource
    list_display = ["pk", "nombre", "apellido", "fecha_nacimiento", "email", "telefono"]
    ordering = [
        "apellido",
        "nombre",
    ]


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "ciudad",
        "telefono",
        "email",
        "sitio_web",
        "fecha_fundacion",
    ]
    list_filter = ["fecha_fundacion"]
    inlines = [
        LibroInline,
    ]



# # Definir la acción personalizada
# def make_published(modeladmin, request, queryset):
#     # Actualizar los objetos seleccionados a "publicados"
#     queryset.update(is_out_of_stock=True)
#     # Mostrar un mensaje informativo en la interfaz de administración
#     modeladmin.message_user(request, "Los libros seleccionados han sido marcados como fuera de stock.")

# # Personalizar el nombre de la acción
# make_published.short_description = "Marcar como fuera de stock"

# # Definir la acción personalizada para exportar a CSV
# def export_posts_to_csv(modeladmin, request, queryset):
#     import csv
#     from django.http import HttpResponse

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="posts.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['Título', 'ISBN', 'Fecha de publicación', 'Número de páginas', 'Idioma'])
#     for post in queryset:
#         writer.writerow([post.titulo, post.isbn, post.fecha_publicacion, post.numero_paginas, post.idioma])
#     return response

# # Personalizar el nombre de la acción
# export_posts_to_csv.short_description = "Exportar libros seleccionados a CSV"




@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "editorial",
        "isbn",
        "fecha_publicacion",
        "numero_paginas",
        "idioma",
    ]
    list_filter = ["editorial", "idioma"]
    search_fields = ["titulo", "autores__nombre"]
    filter_horizontal = ("autores",)
    # actions = [make_published, export_posts_to_csv]
