from . import models
from . import serializers
from rest_framework import viewsets, permissions
from datetime import datetime, time , timedelta 
from rest_framework.exceptions import ValidationError

class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Person class"""

    queryset = models.Person.objects.all()
    serializer_class = serializers.PrsonSerializer
    permission_classes = [permissions.IsAuthenticated]

class File_PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Person.objects.all()
    serializer_class = serializers.File_PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistrationApiView(viewsets.ModelViewSet):
    
    serializer_class = serializers.PrsonSerializer
    def get_queryset(self):
        try:
            from_date=datetime.strptime(self.request.data["from_date"],'%Y-%m-%d')
        except KeyError:
            raise ValidationError(code="from_date_required",detail=("please enter from date"))
        
        to_date =datetime.strptime( self.request.data.get("to_date",datetime.now().strftime("%Y-%m-%d")),'%Y-%m-%d')

        from_date = from_date.replace(hour=0, minute=0, second=0, microsecond=0)
        to_date = to_date.replace(hour=23,minute=59,second=59,microsecond=0)
        return models.Person.objects.filter(created__gte = from_date , created__lte = to_date).count()
