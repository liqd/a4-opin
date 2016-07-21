# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0002_auto_20160708_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='modified',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
