# Generated by Django 4.1.5 on 2023-03-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0012_exercise_profile_exercises"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="Exemple1",
            field=models.TextField(default="None", max_length=500),
        ),
        migrations.AddField(
            model_name="exercise",
            name="Exemple2",
            field=models.TextField(default="None", max_length=500),
        ),
        migrations.AddField(
            model_name="exercise",
            name="Exemple3",
            field=models.TextField(default="None", max_length=500),
        ),
    ]
