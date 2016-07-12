# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0002_auto_20160705_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='title',
            field=models.CharField(max_length=512, default='Title'),
            preserve_default=False,
        ),
    ]
