# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_ideas', '0002_auto_20160715_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
