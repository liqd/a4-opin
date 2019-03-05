# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paragraph',
            options={'ordering': ('weight',)},
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='document',
            field=models.ForeignKey(to='euth_documents.Document', related_name='paragraphs', on_delete=models.CASCADE),
        ),
    ]
