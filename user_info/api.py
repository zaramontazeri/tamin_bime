from . import models
from . import serializers
from rest_framework import viewsets, permissions


class WalletsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Wallets class"""

    queryset = models.Wallets.objects.all()
    serializer_class = serializers.WalletsSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Transactions class"""

    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Invoice class"""

    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


