from rest_framework import serializers
from api.models.buyer_model import Buyer
from django.contrib.auth.models import User

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'