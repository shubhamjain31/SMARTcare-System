# Generated by Django 2.2 on 2019-07-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCareApp', '0006_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Bill_No',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
