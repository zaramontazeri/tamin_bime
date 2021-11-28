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
    list_display = ['created', 'last_updated', 'full_name', 'emergency_numbers', 'national_code', 'gender', 'address_point', 'address', 'company']
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
