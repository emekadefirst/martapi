import secrets
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from api.models.order_model import Order
from .product_model import Product

def generate_reference():
    return secrets.token_hex(8).upper()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    time_purchased = models.DateTimeField(auto_now_add=True)
    

class delivery_address(models.Model):
    buyer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, default=None, related_name='user_delivery_address')
    street = models.TextField(default=None)
    land_mark = models.TextField(default=None)
    LGA = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=15)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class AVAILABLE_PLATFORMS(models.TextChoices):
        PAYSTACK = "PAYSTACK", "Paystack"

    platform = models.CharField(max_length=50, choices=AVAILABLE_PLATFORMS.choices)
    is_active = models.BooleanField(default=False)
    credentials = models.JSONField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='added_transactions')

    description = models.TextField(null=True, blank=True)

    class TRANSACTION_STATUS(models.TextChoices):
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        PENDING = "PENDING", "Pending"
        FAILED = "FAILED", "Failed"

    class TRANSACTION_TYPE(models.TextChoices):
        DEBIT = "DEBIT", "Debit"
        CREDIT = "CREDIT", "Credit"

    status = models.CharField(
        max_length=50,
        choices=TRANSACTION_STATUS.choices,
        default=TRANSACTION_STATUS.PENDING,
    )
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPE.choices)
    reference = models.CharField(max_length=50, default=generate_reference)
    platform_reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Transaction"

    class Meta:
        ordering = ["-created_at"]
