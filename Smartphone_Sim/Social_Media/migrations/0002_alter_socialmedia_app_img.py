# Generated by Django 3.2 on 2021-04-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='app_img',
            field=models.ImageField(default=None, upload_to='static/Images'),
        ),
    ]