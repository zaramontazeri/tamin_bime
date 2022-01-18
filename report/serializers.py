from . import models
from rest_framework import serializers

class CompanyReportSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.CompanyReport
        fields=(
            'pk',
            'created',
            'description',
            'user',
        )