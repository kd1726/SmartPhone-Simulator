# Generated by Django 3.2 on 2021-04-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Media', '0004_alter_socialmedia_app_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='app_img',
            field=models.FilePathField(default=None, path='static/Images'),
        ),
    ]
