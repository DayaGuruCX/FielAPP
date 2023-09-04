
# Generated by Django 4.1.7 on 2023-08-14 15:02
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=150)),
                ('name', models.CharField(blank=True, default='', max_length=150)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('document_type', models.CharField(blank=True, default='', max_length=4)),
                ('document_number', models.CharField(blank=True, default='', max_length=15)),
                ('telephone', models.CharField(blank=True, default='', max_length=12)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('born_date', models.CharField(default='1900-11-11', max_length=30)),
                ('department', models.CharField(blank=True, default='', max_length=50)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('gender', models.CharField(blank=True, default='', max_length=15)),
                ('password', models.CharField(blank=True, default='', max_length=100)),
                ('photo', models.CharField(blank=True, default='', max_length=400)),
                ('object_company', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None)),
                ('clientType', models.BooleanField(blank=True, default=False)),
                ('partnerType', models.BooleanField(blank=True, default=False)),
                ('primaryUser', models.BooleanField(blank=True, default=False))
            ],
        ),
    ]
