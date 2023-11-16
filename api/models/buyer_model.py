import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from api.models.order_model import Order
# from .cart_model import Cart
from .product_model import Product
from .buyer_details_model import History, Order, Cart, delivery_address, Transaction

def generate_reference():
    return secrets.token_hex(8).upper()


class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    phone_number = models.CharField(max_length=15)
    wallet_balance = models.FloatField(max_length=8, default=0.00)
    address = models.OneToOneField(delivery_address, on_delete=models.CASCADE, null=True, default=None, related_name='buyer_address')
    date_created = models.DateTimeField(auto_now_add=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, null=True, default='')
    token = models.CharField(max_length=100, null=True, blank=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, default=None)
    orders = models.ManyToManyField(Order, related_name='buyers', blank=True)
    history = models.ForeignKey(History, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
