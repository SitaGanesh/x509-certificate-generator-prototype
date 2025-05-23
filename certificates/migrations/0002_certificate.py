# Generated by Django 4.2 on 2025-04-07 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("certificates", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificate",
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
                ("name", models.CharField(max_length=100)),
                ("public_key", models.TextField()),
                ("private_key", models.TextField()),
                ("uuid", models.CharField(max_length=36, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="certificates.template",
                    ),
                ),
            ],
        ),
    ]
