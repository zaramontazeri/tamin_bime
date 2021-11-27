from . import models
from . import serializers
from rest_framework import viewsets, permissions

class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Person class"""

    queryset = models.Person.objects.all()
    serializer_class = serializers.PrsonSerializer
    permission_classes = [permissions.IsAuthenticated]