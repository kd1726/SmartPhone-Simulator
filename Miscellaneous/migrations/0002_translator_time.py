# Generated by Django 3.2 on 2021-04-21 23:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Miscellaneous', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translator',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 23, 34, 0, 437405, tzinfo=utc)),
        ),
    ]
