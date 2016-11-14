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
            name='age',
            field=models.SmallIntegerField(verbose_name='Age', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(verbose_name='City', blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(verbose_name='Country of residence', blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(verbose_name='Short description about yourself', blank=True, max_length=250, help_text='This short description will appear on your public profile.'),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_handle',
            field=models.CharField(verbose_name='Facebook name', blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(verbose_name='Gender', blank=True, max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_handle',
            field=models.CharField(verbose_name='Instagram name', blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.CharField(verbose_name='Languages', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_handle',
            field=models.CharField(verbose_name='Twitter name', blank=True, max_length=15),
        ),
    ]
