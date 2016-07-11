# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0005_auto_20160711_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='description_how',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='description_why',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='title',
        ),
    ]
