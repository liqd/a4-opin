# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_offlinephases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offlinephase',
            name='phase',
            field=models.OneToOneField(to='a4phases.Phase', serialize=False, primary_key=True, related_name='offlinephase'),
        ),
    ]
