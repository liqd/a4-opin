# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='result',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='information',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
