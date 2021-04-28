# Generated by Django 3.2 on 2021-04-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('app_img', models.ImageField(default='static/Text.png', upload_to='static/Images')),
                ('link', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
