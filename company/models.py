from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Company(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manager_full_name = models.CharField(max_length=30)
    manager_national_code = models.CharField(max_length=12)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    active = models.BooleanField(default=True)
    phone_numbers = ArrayField(models.CharField(max_length=100,blank=True,null=True))
    capacity = models.IntegerField(default=0)
    address_point = models.PointField()
    address = JSONField(default=dict)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}'
