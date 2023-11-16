from rest_framework import serializers
from models.buyer_details_model import delivery_address

class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = delivery_address
        fields = ['street', 'land_mark', 'LGA', 'zip_code', 'state']
