# Generated by Django 3.1.10 on 2023-05-28 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0010_auto_20230528_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptdb',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
