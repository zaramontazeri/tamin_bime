from django.contrib import admin
from . import models
from django import forms

class CompanyReportAdminForm(forms.ModelForm):

    class Meta:
        model = models.CompanyReport
        fields = '__all__'

class CompanyReportAdmin(admin.ModelAdmin):
    form = CompanyReportAdminForm
    list_display = ['created', 'description', 'user']
    readonly_fields = ['created']

admin.site.register(models.CompanyReport, CompanyReportAdmin)
