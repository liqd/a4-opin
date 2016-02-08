# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectspage_title_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', help_text='The image that is displayed on a projecttile in a project list', to='wagtailimages.Image', null=True),
        ),
    ]
