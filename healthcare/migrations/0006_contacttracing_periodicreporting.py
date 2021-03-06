# Generated by Django 3.0.7 on 2020-08-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0005_auto_20200809_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicReporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('fever_above_100_F', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('cough', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('shortness_of_breath_or_difficulty_breathing', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('sustained_loss_of_smell_or_taste', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('body_aches', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('vomiting_or_diarrhoea', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('patient', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='healthcare.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ContactTracing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.Patient')),
            ],
        ),
    ]
