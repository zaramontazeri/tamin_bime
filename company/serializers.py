from auth_rest_phone.serializers import UserCreatePasswordRetypeSerializer, UsernameRetypeSerializer
from . import models
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_extra_fields.geo_fields import PointField

class CompanySerializer(WritableNestedModelSerializer):
    homeaddress_point=PointField()
    companyaddress_point=PointField()
    user = UserCreatePasswordRetypeSerializer()

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
            'user',
        )
        read_only_fields = ('username',)

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

class InsuranceFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.InsuranceForm
        fields=(
            'pk',
            'created',
            'last_updated',
            'title',
            'description',
            'file'
        )

class InsuranceFormUploadSerializer(serializers.ModelSerializer):
    company_name=serializers.SerializerMethodField()
    class Meta:
        model=models.InsuranceFormUpload
        fields=(
            'pk',
            'created',
            'title',
            'description',
            'file',
            'company_name',
            'company',
            'user',
        )
    def get_company_name(self , obj):
        return obj.company.name