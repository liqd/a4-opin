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
            name='subtitle_da',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_de',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_el',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_en',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_fr',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_it',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_ka',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_mk',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_mt',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_ru',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_sl',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_sv',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='subtitle_uk',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=150),
        ),
    ]
