# Generated by Django 2.2 on 2019-08-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCareApp', '0023_auto_20190807_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='royalty',
            name='Technician_Name',
            field=models.CharField(default='', max_length=50),
        ),
    ]