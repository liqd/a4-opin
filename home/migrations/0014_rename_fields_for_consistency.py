# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20161108_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='menu_title',
            new_name='menu_title_en',
        ),
        migrations.RenameField(
            model_name='rssimport',
            old_name='rss_title',
            new_name='rss_title_en',
        ),
    ]
