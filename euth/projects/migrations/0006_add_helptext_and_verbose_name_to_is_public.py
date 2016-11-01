# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0005_auto_20161024_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(help_text='Please indicate who should be able to participate in your project. Teasers for your project including title and short description will always be visble to everyone', verbose_name='Access to the project', default=True),
        ),
    ]
