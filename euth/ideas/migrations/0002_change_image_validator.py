# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=models.ImageField(validators=[euth.contrib.validators.validate_idea_image], blank=True, upload_to='ideas/images'),
        ),
    ]
