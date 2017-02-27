# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_flashpoll', '0003_change_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashpoll',
            name='key',
            field=models.CharField(max_length=60, verbose_name='Flashpoll ID'),
        ),
    ]
