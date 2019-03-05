# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.offlinephases.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_offlinephases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(null=True, blank=True, editable=False)),
                ('title', models.CharField(max_length=256)),
                ('document', models.FileField(upload_to=euth.offlinephases.models.document_path)),
                ('offlinephase', models.ForeignKey(to='euth_offlinephases.Offlinephase', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
