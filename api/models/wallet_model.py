import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .buyer_model import Buyer



def generate_reference():
    return secrets.token_hex(8).upper()

class Wallet(models.Model):
    user = models.OneToOneField(Buyer, on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

    # class Meta:
    #     ordering = ["-created_at"]
