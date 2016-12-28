# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0003_rename_avatar_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Birthdate'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=80, blank=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, blank=True, verbose_name='Country of residence'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=250, help_text='Write a little bit about yourself. (max. 250 characters)', blank=True, verbose_name='Short description about yourself'),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_handle',
            field=models.CharField(max_length=50, blank=True, verbose_name='Facebook name'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_handle',
            field=models.CharField(max_length=30, blank=True, verbose_name='Instagram name'),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(max_length=150, help_text='Enter the languages you’re speaking.', blank=True, verbose_name='Languages'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_handle',
            field=models.CharField(max_length=15, blank=True, verbose_name='Twitter name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='_avatar',
            field=models.ImageField(upload_to='users/images', blank=True, verbose_name='Avatar'),
        ),
    ]
