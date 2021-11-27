from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField



class Person (models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    full_name = models.CharField(max_length=100)
    emergency_numbers = ArrayField(models.CharField(max_length=100))
    national_code = models.CharField(max_length=10)
    gender = models.CharField(max_length=6,choices=GENDER_TYPE)
    address_point = models.PointField()
    address = JSONField(default=dict)
    files = models.FileField(upload_to="upload/person_files/",null=True,blank=True)

    # Relationship Fields
    company=models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE, related_name="persons"
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.full_name}:{self.national_code}'
