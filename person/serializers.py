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
            'first_name', 
            'last_name',
            'gender',
            'father_name',
            'marital_status',
            'birth_place',
            'Place_issuance_identitycard',
            'marriage_date',
            'birth_date',
            'identity_serialnumber',
            'national_code', 
            'education',
            'job',
            'work_address_point',
            'work_address',
            'address_point', 
            'address', 
            'mobile_numbers',
            'phone_numbers',
            'postalcode',
            'insurance_history',
            'province_registration',
            'province_code',
            'township_registration',
            'township_code',
            'part_registration',
            'part_code',
            'ruraldistrict_registration',
            'ruraldistrict_code',
            'city_registration',
            'city_code',
            'village_registration',

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

