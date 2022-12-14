# Generated by Django 4.1.1 on 2022-10-05 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128, verbose_name='First_Name')),
                ('last_name', models.CharField(blank=True, max_length=128, verbose_name='Last_Name')),
                ('org', models.CharField(blank=True, max_length=128, verbose_name='Organization')),
                ('telephone', models.CharField(blank=True, max_length=50, verbose_name='Telephone')),
                ('birthday', models.DateField(null=True, verbose_name='BirthDay')),
                ('mod_date', models.DateTimeField(auto_now=True, error_messages={'required': ''}, verbose_name='Last modified')),
                ('sex', models.CharField(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default='M', max_length=1, verbose_name='Пол')),
                ('photo', models.ImageField(upload_to='users_avatar/', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]