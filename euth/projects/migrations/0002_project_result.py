# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='result',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
