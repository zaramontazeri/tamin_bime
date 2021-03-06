from django.contrib import admin
from django import forms
from django.contrib.gis.admin.options import OSMGeoAdmin
from .models import  Company, File_Company, InsuranceForm, InsuranceFormUpload
from django.contrib.gis import admin

class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyAdmin(OSMGeoAdmin):
    form = CompanyAdminForm
    list_display = [
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
            ]

admin.site.register(Company, CompanyAdmin)

class FileAdminForm(forms.ModelForm):

    class Meta:
        model = File_Company
        fields = '__all__'

class FileAdmin(admin.ModelAdmin):
    form = FileAdminForm
    list_display = ['created', 'last_updated', 'type','company']
    readonly_fields = ['created', 'last_updated']

admin.site.register(File_Company, FileAdmin)

class InsuranceFormAdminForm(forms.ModelForm):

    class Meta:
        model = InsuranceForm
        fields = '__all__'

class InsuranceFormAdmin(admin.ModelAdmin):
    form = InsuranceFormAdminForm
    list_display = ['created', 'last_updated', 'title','description','file']
    readonly_fields = ['created', 'last_updated']

admin.site.register(InsuranceForm, InsuranceFormAdmin)

class InsuranceFormUploadAdminForm(forms.ModelForm):
    class Meta:
        model=InsuranceFormUpload
        fields='__all__'

class InsuranceFormUploadAdmin(admin.ModelAdmin):
    form=InsuranceFormUploadAdminForm
    list_display=['created','title', 'description', 'company_name', 'file', 'company', 'user']
    readonly_fields=['created']
    
admin.site.register(InsuranceFormUpload, InsuranceFormUploadAdmin)