# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160129_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='adhocracySDK_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
