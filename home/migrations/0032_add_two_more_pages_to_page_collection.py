# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0031_allow_15_pages_in_pagecollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecollection',
            name='page_16',
            field=models.ForeignKey(blank=True, to='wagtailcore.Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='page_17',
            field=models.ForeignKey(blank=True, to='wagtailcore.Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        )
    ]
