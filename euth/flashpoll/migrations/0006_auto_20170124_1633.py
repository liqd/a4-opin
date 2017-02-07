# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_flashpoll', '0005_auto_20170123_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashpoll',
            name='concludeMessage',
        ),
        migrations.RemoveField(
            model_name='flashpoll',
            name='longDescription',
        ),
        migrations.RemoveField(
            model_name='flashpoll',
            name='shortDescription',
        ),
        migrations.RemoveField(
            model_name='flashpoll',
            name='title',
        ),
    ]
