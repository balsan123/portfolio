# Generated by Django 5.1.3 on 2024-11-25 04:06

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Portfolio_app", "0002_userprofile_address_userprofile_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="certification",
            name="date_received",
        ),
        migrations.RemoveField(
            model_name="certification",
            name="institution",
        ),
        migrations.RemoveField(
            model_name="education",
            name="institution",
        ),
        migrations.RemoveField(
            model_name="experience",
            name="company",
        ),
        migrations.RemoveField(
            model_name="project",
            name="date_completed",
        ),
        migrations.RemoveField(
            model_name="project",
            name="link",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="address",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="contact_email",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="contact_phone",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="profile_picture",
        ),
        migrations.AddField(
            model_name="certification",
            name="date_issued",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="certification",
            name="issued_by",
            field=models.CharField(default="Default Issuer", max_length=255),
        ),
        migrations.AddField(
            model_name="certification",
            name="url",
            field=models.URLField(default="http://example.com"),
        ),
        migrations.AddField(
            model_name="education",
            name="description",
            field=models.TextField(default="No description provided"),
        ),
        migrations.AddField(
            model_name="education",
            name="school_name",
            field=models.CharField(default="Default School Name", max_length=255),
        ),
        migrations.AddField(
            model_name="experience",
            name="company_name",
            field=models.CharField(default="Default Company Name", max_length=255),
        ),
        migrations.AddField(
            model_name="project",
            name="url",
            field=models.URLField(default="http://example.com"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="about",
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name="certification",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="certification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="degree",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="education",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="education",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="experience",
            name="role",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="experience",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="skills",
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
