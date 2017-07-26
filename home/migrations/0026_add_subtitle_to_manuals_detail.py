# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_make_linkview_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_da',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_de',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_el',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_en',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_fr',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_it',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_ka',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_mk',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_mt',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_ru',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_sl',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_sv',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='description_uk',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=260),
        ),
    ]
