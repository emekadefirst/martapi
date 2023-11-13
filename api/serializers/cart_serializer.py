from rest_framework import serializers
from models.cart_model import Cart



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = "__all__"