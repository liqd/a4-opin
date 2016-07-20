# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0002_auto_20160715_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
