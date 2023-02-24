# Generated by Django 4.1.5 on 2023-02-20 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users_app", "0002_todo_list"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=500, null=True)),
                (
                    "short_intro",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        default="profiles/default_profile.png",
                        null=True,
                        upload_to="profiles/",
                    ),
                ),
                (
                    "social_github",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_twitter",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_linkedin",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_youtube",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "social_website",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="CreateUserModel",
        ),
    ]
