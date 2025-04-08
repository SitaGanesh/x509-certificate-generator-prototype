# Generated by Django 4.2 on 2025-04-07 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Template",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("generic", "Generic"),
                            ("certificate", "Certificate"),
                        ],
                        max_length=16,
                    ),
                ),
                (
                    "ca_name",
                    models.CharField(
                        blank=True,
                        help_text="Certificate Authority name",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(
                        blank=True, help_text="Duration in days", null=True
                    ),
                ),
                (
                    "key_length",
                    models.IntegerField(
                        blank=True, choices=[(2048, "2048"), (4096, "4096")], null=True
                    ),
                ),
                (
                    "digest_algorithm",
                    models.CharField(
                        blank=True,
                        choices=[("sha256", "SHA-256"), ("sha512", "SHA-512")],
                        max_length=8,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
