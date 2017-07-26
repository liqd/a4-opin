# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_add_maltese'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link_view',
            field=models.CharField(max_length=100, blank=True, default='', choices=[('organisation-list', 'List of Organisations')]),
            preserve_default=False,
        ),
    ]
