# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_flashpoll', '0004_auto_20170109_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashpoll',
            name='concludeMessage',
            field=models.CharField(verbose_name='Conclude message', null=True, max_length=60, blank=True),
        ),
        migrations.AddField(
            model_name='flashpoll',
            name='longDescription',
            field=models.TextField(verbose_name='Long description', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flashpoll',
            name='shortDescription',
            field=models.TextField(verbose_name='Subtitle', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flashpoll',
            name='title',
            field=models.CharField(verbose_name='Title', null=True, max_length=60, blank=True),
        ),
    ]
