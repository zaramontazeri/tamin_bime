# Generated by Django 3.2.5 on 2022-02-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_company_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('file', models.FileField(upload_to='upload/insuranceform_file')),
            ],
        ),
    ]