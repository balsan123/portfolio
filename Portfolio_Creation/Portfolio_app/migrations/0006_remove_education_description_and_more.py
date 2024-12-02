# Generated by Django 5.1.3 on 2024-11-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Portfolio_app", "0005_logintable"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="education",
            name="description",
        ),
        migrations.RemoveField(
            model_name="education",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="education",
            name="start_date",
        ),
        migrations.AddField(
            model_name="education",
            name="others",
            field=models.TextField(blank=True, default="others if exist", null=True),
        ),
        migrations.AddField(
            model_name="education",
            name="yop",
            field=models.IntegerField(default=2024),
        ),
    ]