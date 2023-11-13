from rest_framework import serializers
from models.wallet_model import Wallet



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        field = "__all__"