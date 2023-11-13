from rest_framework import serializers
from models.History_model import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        field = "__all__"