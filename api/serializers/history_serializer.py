from rest_framework import serializers
from api.models.buyer_model import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"