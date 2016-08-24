# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0007_auto_20160715_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='facebook_handle',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='instagram_handle',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='twitter_handle',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='webpage',
            field=models.URLField(blank=True),
        ),
    ]
