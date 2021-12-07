from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Company(models.Model):
    MAINSTREET='mainstreet' #asli
    AUXILIARYROAD='auxiliaryroad' #farei
    DOWNTOWN='downtown' #markaz
    CITYENTRANCEEXIT='city_entrance/exit' #vorodi/khorogi shahr
    SUBRUBS='suburbs' #hoomeh
    LOCATION_TYPE=((MAINSTREET,MAINSTREET),(AUXILIARYROAD,AUXILIARYROAD),(DOWNTOWN,DOWNTOWN),(CITYENTRANCEEXIT,CITYENTRANCEEXIT),(SUBRUBS,SUBRUBS))
    # Fields
    date_completion=models.DateField()
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manager_first_name = models.CharField(max_length=30)
    manager_last_name = models.CharField(max_length=30,null=True,blank=True)
    manager_national_code = models.CharField(max_length=12)
    main_field_activity=models.CharField(max_length=300)
    experience=models.TextField()
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    active = models.BooleanField(default=True)
    mobile_numbers = ArrayField(models.CharField(max_length=100))
    phone_numbers = ArrayField(models.CharField(max_length=100))
    homeaddress_point = models.PointField()
    homeaddress = JSONField(default=dict)
    companyaddress_point = models.PointField()
    companyaddress = JSONField(default=dict)
    province=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    company_postalcode=models.CharField(max_length=20)
    company_phone_numbers_code=ArrayField(models.CharField(max_length=100))
    company_fax=models.CharField(max_length=50)
    permits_ratings=models.TextField()
    location=models.CharField(choices=LOCATION_TYPE,max_length=20)
    businesslicense_type=models.CharField(max_length=100)
    establishment_date=models.DateField()
    business_license_number=models.CharField(max_length=50)
    business_license_place=models.CharField(max_length=50)
    license_expiration_date=models.CharField(max_length=50)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}'

class File_Company (models.Model):
    MOHR='mohr'
    EMZA='emza'
    FILE_TYPE=((MOHR,MOHR),(EMZA,EMZA))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type= models.CharField(max_length=20,choices=FILE_TYPE)
    files = models.FileField(upload_to="upload/company_files/")
    # Relationship Fields
    company=models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE, related_name="files"
    )
    class Meta:
        ordering = ('-created',)
        verbose_name = ('File')
        verbose_name_plural = ('Files')

    def __str__(self):
        return f'{self.company.name}'
