from rest_framework import serializers
from models.category_model import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"