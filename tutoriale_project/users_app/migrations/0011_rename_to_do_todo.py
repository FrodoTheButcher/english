# Generated by Django 4.1.5 on 2023-02-20 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0010_to_do"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="To_do",
            new_name="todo",
        ),
    ]
