# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('a4phases', '0004_change_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offlinephase',
            fields=[
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(null=True, editable=False, blank=True)),
                ('text', ckeditor.fields.RichTextField()),
                ('phase', models.OneToOneField(primary_key=True, to='a4phases.Phase', serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
