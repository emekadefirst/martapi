from rest_framework import serializers
from api.models.buyer_model import Buyer
from django.contrib.auth.models import User 
from api.models.buyer_details_model import delivery_address

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Buyer
		fields = '__all__'

class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = delivery_address
        fields = ['street', 'land_mark', 'LGA', 'zip_code', 'state']
