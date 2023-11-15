import secrets
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        permissions = [
            ("view_category_custom", "Can view categories"),
            ("add_category_custom", "Can add categories"),
            ("change_category_custom", "Can change categories"),
            ("delete_category_custom", "Can delete categories"),
        ]
        