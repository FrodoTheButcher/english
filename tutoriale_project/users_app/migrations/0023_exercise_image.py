# Generated by Django 4.1.5 on 2023-03-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0022_exercise_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="Image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
