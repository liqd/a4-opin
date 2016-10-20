# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_phases', '0003_shorten_phase_description_and_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='phase',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
