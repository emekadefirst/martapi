from rest_framework import serializers
from models.order_model import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = "__all__"