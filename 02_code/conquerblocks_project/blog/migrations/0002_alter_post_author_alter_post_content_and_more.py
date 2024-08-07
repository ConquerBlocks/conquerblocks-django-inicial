# Generated by Django 5.0.7 on 2024-08-02 16:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.CharField(max_length=100, verbose_name="Autor"),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(verbose_name="Contenido"),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Fecha y hora de creación",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
    ]
