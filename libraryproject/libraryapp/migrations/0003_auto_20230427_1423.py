# Generated by Django 3.1.10 on 2023-04-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20230425_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindb',
            name='Address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logindb',
            name='Mobile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logindb',
            name='Phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
