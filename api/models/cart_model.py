import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .buyer_model import Buyer
from .product_model import Product

def generate_reference():
    return secrets.token_hex(8).upper()

class Cart(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now_add=True)

