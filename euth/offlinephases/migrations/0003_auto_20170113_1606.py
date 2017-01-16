# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_offlinephases', '0002_auto_20170113_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offlinephase',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
