from django.contrib import admin
from django import forms
from django.contrib.gis.admin.options import OSMGeoAdmin
from .models import  File_Person, Person

class PersonAdminForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

class PersonAdmin(OSMGeoAdmin):
    form = PersonAdminForm
    list_display = ['created', 'last_updated', 'first_name','last_name','gender','father_name','marital_status','birth_place','Place_issuance_identitycard','marriage_date', 'birth_date', 'identity_serialnumber','identity_number', 'national_code','education',
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
            'village_registration', 'company','company_name'
            ]
    readonly_fields = ['created', 'last_updated']

admin.site.register(Person, PersonAdmin)

class FileAdminForm(forms.ModelForm):

    class Meta:
        model = File_Person
        fields = '__all__'

class FileAdmin(admin.ModelAdmin):
    form = FileAdminForm
    list_display = ['created', 'last_updated', 'type','person']
    readonly_fields = ['created', 'last_updated']

admin.site.register(File_Person, FileAdmin)
