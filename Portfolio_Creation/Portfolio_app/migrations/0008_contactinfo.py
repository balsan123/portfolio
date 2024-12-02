# Generated by Django 5.1.3 on 2024-11-25 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Portfolio_app", "0007_userprofile_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "user_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Portfolio_app.userprofile",
                    ),
                ),
            ],
        ),
    ]