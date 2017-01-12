# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4phases', '0004_auto_20170112_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offlinephase',
            fields=[
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(editable=False, blank=True, null=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('phase', models.OneToOneField(primary_key=True, serialize=False, to='a4phases.Phase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
