# Generated by Django 5.1.3 on 2024-11-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "Portfolio_app",
            "0004_alter_education_end_date_alter_education_start_date_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginTable",
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
                ("username", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("password1", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
            ],
        ),
    ]
