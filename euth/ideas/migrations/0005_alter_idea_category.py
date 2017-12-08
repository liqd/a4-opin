# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.categories.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('euth_ideas', '0004_change_category_and_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='category',
            field=adhocracy4.categories.fields.CategoryField(to='a4categories.Category', related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True),
        ),
    ]
