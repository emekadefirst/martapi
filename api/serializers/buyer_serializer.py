from rest_framework import serializers
from models.buyer_model import Buyer

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        field = "__all__"