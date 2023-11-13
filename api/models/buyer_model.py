import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

def generate_reference():
    return secrets.token_hex(8).upper()

class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    
    phone_number = models.CharField(max_length=15)
    profile_image = models.FileField(upload_to="buyer-img-store")
    wallet_balance = models.FloatField(max_length=8, default=0.00)
    street_address = models.TextField(default=None)
    land_mark = models.TextField(default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    LGA = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username
    