# Generated by Django 5.0.7 on 2024-08-13 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_contact_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="commentario",
            new_name="comentario",
        ),
    ]
