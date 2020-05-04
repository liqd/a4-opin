# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators
import euth.offlinephases.models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_offlinephases', '0002_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='document',
            field=models.FileField(upload_to=euth.offlinephases.models.document_path, validators=[
                euth.contrib.validators.validate_file_type_and_size]),
        ),
        migrations.AlterField(
            model_name='offlinephase',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
