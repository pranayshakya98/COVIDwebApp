# Generated by Django 3.0.7 on 2020-08-10 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0008_auto_20200809_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='pick_Time_Slot',
            field=models.CharField(blank=True, choices=[('8am-9am', '8am-9am'), ('9am-10am', '9am-10am'), ('10am-11am', '10am-11am'), ('11am-12pm', '11am-12pm'), ('12pm-1pm', '12pm-1pm'), ('1pm-2pm', '1pm-2pm'), ('2pm-3pm', '2pm-3pm'), ('3pm-4pm', '3pm-4pm'), ('4pm-5pm', '4pm-5pm'), ('5pm-6pm', '5pm-6pm'), ('6pm-7pm', '6pm-7pm'), ('7pm-8pm', '7pm-8pm'), ('8pm-9pm', '8pm-9pm')], max_length=10),
        ),
    ]
