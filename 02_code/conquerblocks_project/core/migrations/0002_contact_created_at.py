# Generated by Django 5.0.7 on 2024-08-13 16:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Fecha y hora de creación",
            ),
        ),
    ]
