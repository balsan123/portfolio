# Generated by Django 5.1.3 on 2024-11-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Portfolio_app", "0006_remove_education_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
