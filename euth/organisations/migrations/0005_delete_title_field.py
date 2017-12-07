# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0004_copy_english_title_to_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisationtranslation',
            name='title',
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name',
            field=models.CharField(unique=True, verbose_name='title', max_length=512),
        ),
    ]
