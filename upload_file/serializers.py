from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "store_owner",
            "store_name",
        )