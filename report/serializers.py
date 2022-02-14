from . import models
from rest_framework import serializers

class CompanyReportSerializers(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    # def _user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return request.user
    class Meta:
        model=models.CompanyReport
        fields=(
            'pk',
            'created',
            'description',
            'user',
        )