# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0002_auto_20160912_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='result',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
