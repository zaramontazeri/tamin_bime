from . import models
from . import serializers
from rest_framework import viewsets, permissions

class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class File_CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Company.objects.all()
    serializer_class = serializers.File_CompanySerializer
    permission_classes = [permissions.IsAuthenticated]