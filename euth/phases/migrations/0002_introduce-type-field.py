# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.phases.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_phases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phase',
            old_name='permissions',
            new_name='type'
        ),
        migrations.AlterField(
            model_name='phase',
            name='type',
            field=models.CharField(max_length=128, validators=[euth.phases.validators.validate_content]),
        ),
    ]
