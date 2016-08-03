# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_rates', '0002_auto_20160803_1409'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('object_pk', 'user'), ('content_type', 'user')]),
        ),
    ]
