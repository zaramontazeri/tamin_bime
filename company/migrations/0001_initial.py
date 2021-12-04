# Generated by Django 3.2.9 on 2021-12-04 14:30

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completion', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('manager_first_name', models.CharField(max_length=30)),
                ('manager_last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('manager_national_code', models.CharField(max_length=12)),
                ('main_field_activity', models.CharField(max_length=300)),
                ('experience', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('mobile_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('phone_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('homeaddress_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('homeaddress', models.JSONField(default=dict)),
                ('companyaddress_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('companyaddress', models.JSONField(default=dict)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('company_postalcode', models.CharField(max_length=20)),
                ('company_phone_numbers_code', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('company_fax', models.CharField(max_length=50)),
                ('permits_ratings', models.TextField()),
                ('location', models.CharField(choices=[('mainstreet', 'mainstreet'), ('auxiliaryroad', 'auxiliaryroad'), ('downtown', 'downtown'), ('city_entrance/exit', 'city_entrance/exit'), ('suburbs', 'suburbs')], max_length=20)),
                ('businesslicense_type', models.CharField(max_length=100)),
                ('establishment_date', models.DateField()),
                ('business_license_number', models.CharField(max_length=50)),
                ('business_license_place', models.CharField(max_length=50)),
                ('license_expiration_date', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='File_Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('mohr', 'mohr'), ('emza', 'emza')], max_length=20)),
                ('files', models.FileField(upload_to='upload/company_files/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='company.company')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ('-created',),
            },
        ),
    ]
