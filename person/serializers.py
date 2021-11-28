from . import models
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

class PrsonSerializer(serializers.ModelSerializer):
    address_point = PointField()
    class Meta:
        
        model = models.Person
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'full_name', 
            'emergency_numbers', 
            'national_code', 
            'gender', 
            'address_point', 
            'address', 
        )

class File_PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.File_Person
        fields=(
            'pk',
            'created', 
            'last_updated',
            'type',
            'files',
            'person'
        )