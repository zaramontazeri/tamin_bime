from . import models
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_extra_fields.geo_fields import PointField

class CompanySerializer(WritableNestedModelSerializer):
    homeaddress_point=PointField()
    companyaddress_point=PointField()

    class Meta:
        model = models.Company
        fields = (
            'pk', 
            'date_completion',
            'created', 
            'last_updated', 
            'manager_first_name', 
            'manager_last_name',
            'manager_national_code', 
            'name', 
            'main_field_activity',
            'experience',
            'email', 
            'website', 
            'active', 
            'phone_numbers', 
            'homeaddress',
            'homeaddress_point',
            'mobile_numbers',
            'companyaddress',
            'companyaddress_point',
            'province',
            'city',
            'company_postalcode',
            'company_phone_numbers_code',
            'company_fax',
            'permits_ratings',
            'location',
            'businesslicense_type',
            'establishment_date',
            'business_license_number',
            'business_license_place',
            'license_expiration_date',
            'username',
        )

class File_CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.File_Company
        fields=(
            'pk',
            'created', 
            'last_updated',
            'type',
            'files',
            'company'
        )