# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('euth_ideas', '0002_change_image_validator'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='a4categories.Category'),
        ),
    ]
