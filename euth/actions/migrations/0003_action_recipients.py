# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_actions', '0002_make_user_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='recipients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
