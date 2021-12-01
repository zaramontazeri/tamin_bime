from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Person (models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    MARRIED="married"
    SINGLE="single"
    MARITAL_STATUS_TYPE=((MARRIED,MARRIED),(SINGLE,SINGLE))
    BISAVAD="bisavad"
    EBTEDAEI="ebtedaei"
    SICL="sicl"
    DIPLOM="diplom"
    KARDANI="kardani"
    KARSHENASI="karshenasi"
    KARSHENASIARSHAD="karshenasiarshad"
    DOCTORA="doctora"
    EDUCATION_TYPE=((BISAVAD,BISAVAD),(EBTEDAEI,EBTEDAEI),(SICL,SICL),(DIPLOM,DIPLOM),(KARDANI,KARDANI),(KARSHENASI,KARSHENASI),(KARSHENASIARSHAD,KARSHENASIARSHAD),(DOCTORA,DOCTORA))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER_TYPE)
    father_name = models.CharField(max_length=50)
    marital_status=models.CharField(max_length=7,choices=MARITAL_STATUS_TYPE)
    birth_place=models.CharField(max_length=50)
    Place_issuance_identitycard=models.CharField(max_length=50)
    marriage_date=models.DateField(null=True,blank=True)
    birth_date=models.DateField()
    identity_serialnumber=models.CharField(max_length=10)
    national_code = models.CharField(max_length=10)
    education=models.CharField(max_length=20,choices=EDUCATION_TYPE)
    job=models.CharField(max_length=50)
    work_address_point=models.PointField()
    work_address = JSONField(default=dict)
    address_point = models.PointField()
    address = JSONField(default=dict)
    mobile_numbers = ArrayField(models.CharField(max_length=100))
    phone_numbers = ArrayField(models.CharField(max_length=100, null=True,blank=True))
    postalcode=models.CharField(max_length=10)
    insurance_history= models.BooleanField(default=False)
    province_registration=models.CharField(max_length=50)
    province_code=models.CharField(max_length=5)
    township_registration=models.CharField(max_length=50)
    township_code=models.CharField(max_length=5)
    part_registration=models.CharField(max_length=50)
    part_code=models.CharField(max_length=5)
    ruraldistrict_registration=models.CharField(max_length=50,null=True,blank=True)
    ruraldistrict_code=models.CharField(max_length=5)
    city_registration=models.CharField(max_length=50)
    city_code=models.CharField(max_length=5)
    village_registration=models.CharField(max_length=50,null=True,blank=True)
    

    # Relationship Fields
    company=models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE, related_name="persons"
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}:{self.national_code}'

class File_Person (models.Model):
    SHENASNAMEH= "shenasnameh"
    CARTMELI ="cartmeli"
    IMAGE="image"
    FILE_TYPE = ((SHENASNAMEH,SHENASNAMEH),(CARTMELI,CARTMELI),(IMAGE,IMAGE))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type= models.CharField(max_length=20,choices=FILE_TYPE)
    files = models.FileField(upload_to="upload/person_files/")
    # Relationship Fields
    person=models.ForeignKey(
        'person.Person',
        on_delete=models.CASCADE, related_name="files"
    )
    class Meta:
        ordering = ('-created',)
        verbose_name = ('File')
        verbose_name_plural = ('Files')

    def __str__(self):
        return f'{self.person.firstname} {self.person.lastname}'
