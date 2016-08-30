# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0008_add-social-share'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, default='ME'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='place',
            field=models.CharField(max_length=200, default='unknown'),
            preserve_default=False,
        ),
    ]
