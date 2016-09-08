# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_comments', '0002_auto_20160712_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
