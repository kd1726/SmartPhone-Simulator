# Generated by Django 3.2 on 2021-04-16 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communication', '0005_auto_20210415_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='home_number',
            field=models.CharField(default=' ', max_length=18),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='work_number',
            field=models.CharField(default=' ', max_length=18),
        ),
    ]