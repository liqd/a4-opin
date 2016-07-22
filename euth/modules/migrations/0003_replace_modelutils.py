# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0002_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='modified',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
