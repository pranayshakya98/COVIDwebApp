# Generated by Django 3.0.7 on 2020-08-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0014_medication_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='description',
            field=models.TextField(),
        ),
    ]