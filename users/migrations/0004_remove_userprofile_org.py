# Generated by Django 4.1.1 on 2022-10-22 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_city_userprofile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='org',
        ),
    ]
