# Generated by Django 3.2.5 on 2022-02-21 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0010_insuranceform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceform',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='InsuranceFormUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('file', models.FileField(upload_to='upload/insuranceformupload_file')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insuranceFormUploads', to='company.company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insuranceFormUploads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
