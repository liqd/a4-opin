# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(editable=False, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified',
            field=models.DateTimeField(editable=False, blank=True, null=True),
        ),
    ]
