# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_phases', '0002_introduce-type-field'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phase',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
