import secrets
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver


# def generate_reference():
#     return secrets.token_hex(8).upper()

class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        permissions = [
            ("view_category_custom", "Can view categories"),
            ("add_category_custom", "Can add categories"),
            ("change_category_custom", "Can change categories"),
            ("delete_category_custom", "Can delete categories"),
        ]
        