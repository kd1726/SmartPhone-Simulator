# Generated by Django 3.2 on 2021-04-22 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Miscellaneous', '0003_auto_20210421_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translator',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 17, 59, 29, 328514, tzinfo=utc)),
        ),
    ]
