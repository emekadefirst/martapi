# Generated by Django 4.2.7 on 2023-11-16 07:32

import api.models.buyer_details_model
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0008_buyer_history_alter_history_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="delivery_address",
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
                ("street", models.TextField(default=None)),
                ("land_mark", models.TextField(default=None)),
                ("LGA", models.CharField(max_length=50)),
                ("zip_code", models.IntegerField()),
                ("state", models.CharField(max_length=15)),
                (
                    "buyer",
                    models.OneToOneField(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_delivery_address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("transaction_id", models.CharField(default="", max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "platform",
                    models.CharField(choices=[("PAYSTACK", "Paystack")], max_length=50),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("credentials", models.JSONField()),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("SUCCESSFUL", "Successful"),
                            ("PENDING", "Pending"),
                            ("FAILED", "Failed"),
                        ],
                        default="PENDING",
                        max_length=50,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("DEBIT", "Debit"), ("CREDIT", "Credit")],
                        max_length=50,
                    ),
                ),
                (
                    "reference",
                    models.CharField(
                        default=api.models.buyer_details_model.generate_reference,
                        max_length=50,
                    ),
                ),
                ("platform_reference", models.CharField(blank=True, max_length=100)),
                (
                    "added_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="added_transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.RemoveField(
            model_name="buyer",
            name="LGA",
        ),
        migrations.RemoveField(
            model_name="buyer",
            name="land_mark",
        ),
        migrations.RemoveField(
            model_name="buyer",
            name="state",
        ),
        migrations.RemoveField(
            model_name="buyer",
            name="street_address",
        ),
        migrations.DeleteModel(
            name="Wallet",
        ),
        migrations.AddField(
            model_name="buyer",
            name="address",
            field=models.OneToOneField(
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="buyer_address",
                to="api.delivery_address",
            ),
        ),
        migrations.AddField(
            model_name="buyer",
            name="transaction",
            field=models.OneToOneField(
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.transaction",
            ),
        ),
    ]