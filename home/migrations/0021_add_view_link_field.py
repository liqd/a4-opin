# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepage_add_editable_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link_view',
            field=models.CharField(blank=True, max_length=100, choices=[('organisation-list', 'List of Organisations')], null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, to='wagtailcore.Page', null=True, related_name='+', on_delete=models.CASCADE),
        ),
    ]
