# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4phases', '0004_change_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offlinephase',
            fields=[
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(editable=False, null=True, blank=True)),
                ('text', ckeditor.fields.RichTextField(blank=True)),
                ('phase', models.OneToOneField(to='a4phases.Phase', related_name='offlinephase', serialize=False, primary_key=True, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
