from . import models
from . import serializers
from rest_framework import viewsets, permissions

class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]