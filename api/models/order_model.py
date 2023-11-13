import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .product_model import Product


def generate_reference():
    return secrets.token_hex(8).upper()

class Order(models.Model):
    class ORDER_STATUS(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    reference = models.CharField(max_length=50, default=generate_reference)
    # transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS.choices, default=ORDER_STATUS.PENDING
    )

