from . import models
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CompanySerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Company
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'manager_first_name', 
            'manager_last_name',
            'manager_national_code', 
            'name', 
            'email', 
            'website', 
            'active', 
            'phone_numbers', 
            'address'
        )