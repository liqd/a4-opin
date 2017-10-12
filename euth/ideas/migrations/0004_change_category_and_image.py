# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.images.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('euth_ideas', '0003_idea_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='category',
            field=models.ForeignKey(related_name='+', to='a4categories.Category', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('idea_image', upload_to='ideas/images', blank=True),
        ),
    ]
