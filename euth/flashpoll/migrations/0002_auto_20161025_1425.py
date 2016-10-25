# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_flashpoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashpoll',
            name='key',
            field=models.CharField(verbose_name='Flashpoll ID', max_length=30),
        ),
    ]
