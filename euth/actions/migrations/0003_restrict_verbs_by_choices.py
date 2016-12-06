# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_actions', '0002_make_user_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='verb',
            field=models.CharField(max_length=255, choices=[('complete', 'COMPLETE'), ('create', 'CREATE'), ('update', 'UPDATE')], db_index=True),
        ),
    ]
