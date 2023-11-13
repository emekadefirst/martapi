import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .category_model import Category



def generate_reference():
    return secrets.token_hex(8).upper()

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.FileField(upload_to="Product-img-store")
    date_created = models.DateTimeField(auto_now_add=True)
    product_description = models.TextField(default='')
    

    class Meta:
        permissions = [
            ("view_product_custom", "Can view products"),
            ("add_product_custom", "Can add products"),
            ("change_product_custom", "Can change products"),
            ("delete_product_custom", "Can delete products"),
        ]
        ordering = ['-date_created']

    def __str__(self):
        return self.name
