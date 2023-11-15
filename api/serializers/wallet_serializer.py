from rest_framework import serializers
from api.models.buyer_model import Wallet



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"