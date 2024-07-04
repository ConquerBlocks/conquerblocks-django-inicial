# Generated by Django 5.0.6 on 2024-06-28 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_alter_person_family"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="family",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to="todos.family",
            ),
        ),
    ]