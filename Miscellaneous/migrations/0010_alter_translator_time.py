# Generated by Django 3.2 on 2021-05-01 00:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Miscellaneous', '0009_alter_translator_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translator',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 0, 47, 24, 449548, tzinfo=utc)),
        ),
    ]