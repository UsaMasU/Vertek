# Generated by Django 3.1 on 2020-09-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_departmentperson_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='departmentperson',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
