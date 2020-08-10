# Generated by Django 3.0.7 on 2020-08-10 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0010_periodicreporting_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodicreporting',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='healthcare.Patient'),
        ),
    ]
