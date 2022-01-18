from . import models
from . import serializers
from rest_framework import viewsets, permissions

class CompanyReportViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company Report class"""

    queryset = models.CompanyReport.objects.all()
    serializer_class = serializers.CompanyReportSerializers
    permission_classes = [permissions.IsAuthenticated]