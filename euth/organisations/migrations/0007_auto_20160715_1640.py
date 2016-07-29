# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0006_auto_20160711_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='modified',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
