# Generated by Django 2.2 on 2019-12-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCareApp', '0025_auto_20190810_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
                ('Account_Type', models.IntegerField()),
            ],
        ),
    ]
