import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from api.models.order_model import Order
# from .cart_model import Cart
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

class Buyer(models.Model):
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    wallet_balance = models.FloatField(max_length=8, default=0.00)
    street_address = models.TextField(default=None)
    land_mark = models.TextField(default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    LGA = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, default=None)
    orders = models.ManyToManyField(Order, related_name='buyers', blank=True)
    history = models.ForeignKey(History, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

# Move import statement to the end

import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .buyer_model import Buyer, Cart


def generate_reference():
    return secrets.token_hex(8).upper()


    
    
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .product_model import Product


def generate_reference():
    return secrets.token_hex(8).upper()


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
