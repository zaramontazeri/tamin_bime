from . import models
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField


class PrsonSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()  #add to serializer with def get() to get company_name
    address_point = PointField()  #add to serializer to send location from map as lat and long
    work_address_point=PointField()
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
            'identity_number',
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
            'company',
            'company_name'
            

        )
    def get_company_name(self , obj):
        return obj.company.name

class File_PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.File_Person
        fields=(
            'pk',
            'created', 
            'last_updated',
            'type',
            'person_document',
            'person'
        )