# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_flashpoll', '0002_add_verbose_name_to_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashpoll',
            name='module',
            field=models.OneToOneField(related_name='flashpoll_settings', to='euth_modules.Module'),
        ),
    ]
