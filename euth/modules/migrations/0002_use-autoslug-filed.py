# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, populate_from='name', editable=False),
        ),
    ]
