from . import models

from rest_framework import serializers


class WalletsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallets
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'value', 
        )


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = "__all__"


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invoice
        fields = (
            'pk', 
            'created', 
            'last_updated', 
        )


