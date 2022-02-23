from django.conf import settings
from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField


class Company(models.Model):
    MAINSTREET = 'MAINSTREET'  # asli
    AUXILIARYROAD = 'AUXILIARYROAD'  # farei
    DOWNTOWN = 'DOWNTOWN'  # markaz
    CITYENTRANCEEXIT = 'CITYENTRANCEEXIT'  # vorodi/khorogi shahr
    SUBRUBS = 'SUBRUBS'  # hoomeh
    LOCATION_TYPE = ((MAINSTREET, MAINSTREET), (AUXILIARYROAD, AUXILIARYROAD),
                     (DOWNTOWN, DOWNTOWN), (CITYENTRANCEEXIT, CITYENTRANCEEXIT), (SUBRUBS, SUBRUBS))
    # Fields
    date_completion = models.DateField()
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manager_first_name = models.CharField(max_length=30)
    manager_last_name = models.CharField(max_length=30)
    manager_national_code = models.CharField(max_length=12)
    main_field_activity = models.CharField(max_length=300)
    experience = models.TextField()
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    active = models.BooleanField(default=True)
    mobile_numbers = ArrayField(models.CharField(max_length=100))
    phone_numbers = ArrayField(models.CharField(max_length=100))
    homeaddress_point = models.PointField(blank=True, null=True)
    homeaddress = models.CharField(max_length=100, null=True, blank=True)
    companyaddress_point = models.PointField(blank=True, null=True)
    companyaddress = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    company_postalcode = models.CharField(max_length=20)
    company_phone_numbers_code = ArrayField(models.CharField(max_length=100))
    company_fax = models.CharField(max_length=50)
    permits_ratings = models.TextField()
    location = models.CharField(choices=LOCATION_TYPE, max_length=20)
    businesslicense_type = models.CharField(max_length=100)
    establishment_date = models.DateField()
    business_license_number = models.CharField(max_length=50)
    business_license_place = models.CharField(max_length=50)
    license_expiration_date = models.DateField()
    username = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='companies', null=True, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.pk} : {self.name}'


class File_Company (models.Model):
    MOHR = 'mohr'
    EMZA = 'emza'
    FILE_TYPE = ((MOHR, MOHR), (EMZA, EMZA))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=20, choices=FILE_TYPE)
    files = models.FileField(upload_to="upload/company_files/")
    # Relationship Fields
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE, related_name="files"
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = ('File')
        verbose_name_plural = ('Files')

    def __str__(self):
        return f'{self.company.name}'


class InsuranceForm(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    file = models.FileField(upload_to="upload/insuranceform_file")


class InsuranceFormUpload(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    file = models.FileField(upload_to="upload/insuranceformupload_file")
    company_name = models.CharField(max_length=50, null=True, blank=True)

    # Relationship Fields
    company = models.ForeignKey(
        'company.Company', on_delete=models.CASCADE, related_name="insuranceFormUploads_company")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name="insuranceFormUploads_user", null=True, blank=True)

    class Meta:
        ordering = ('-created',)