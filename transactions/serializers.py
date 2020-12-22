from rest_framework import serializers

from .models import Transaction
from django.core.exceptions import ValidationError


class TransactionSerializer(serializers.ModelSerializer):
    def validate(self, data):

        # would prefer this (self-validating model), but not working
        # instance = Transaction(data)
        # instance.clean()

        if data["from_account"].id == data["to_account"].id:
            raise ValidationError("from account cannot be to account")

        return data

    class Meta:
        model = Transaction
        fields = ("id", "trans_date", "amount", "from_account", "to_account")
