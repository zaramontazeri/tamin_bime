from django.contrib import admin
from django import forms
from django.contrib.gis.admin.options import OSMGeoAdmin
from .models import  Company
from django.contrib.gis import admin

class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyAdmin(OSMGeoAdmin):
    form = CompanyAdminForm
    list_display = ['created', 'last_updated','name', 'manager_full_name', 'manager_national_code', 'email', 'website', 'active', 'phone_numbers', 'address_point', 'address']

admin.site.register(Company, CompanyAdmin)
