# Generated by Django 4.2.7 on 2023-11-15 07:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="buyer",
            name="profile_image",
        ),
    ]
