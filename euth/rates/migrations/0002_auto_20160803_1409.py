# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_rates', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('content_type', 'object_pk', 'user')]),
        ),
    ]
