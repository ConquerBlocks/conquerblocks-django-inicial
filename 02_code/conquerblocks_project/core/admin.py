from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ("nombre", "contactado", "email", "created_at")
    list_filter = ("contactado", )
