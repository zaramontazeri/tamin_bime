from django.db import models
from django.conf import settings
class CompanyReport(models.Model):
    # Fields
    created=models.DateTimeField(auto_now_add=True, editable=False)
    description=models.TextField(max_length=1000)

    # Relationship Fields
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='companyreport')
    
    class Meta:
        ordering=('-created',)


