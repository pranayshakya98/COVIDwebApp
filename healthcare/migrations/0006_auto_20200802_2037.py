# Generated by Django 3.0.7 on 2020-08-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0005_auto_20200802_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='allergyInfo',
        ),
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact_phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='insurance_provider',
            field=models.CharField(max_length=200, null=True),
        ),
    ]