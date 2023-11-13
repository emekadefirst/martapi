import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .buyer_model import Buyer
from .cart_model import Cart

def generate_reference():
    return secrets.token_hex(8).upper()

class History(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    time_purchased = models.DateTimeField(auto_now_add=True)
    