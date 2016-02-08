# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_adhocracyprojectpage_adhocracysdk_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectspage',
            name='title_en',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
