# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=models.ImageField(blank=True, upload_to='organisations/images', validators=[euth.contrib.validators.validate_hero_image]),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(blank=True, upload_to='organisations/logos', validators=[euth.contrib.validators.validate_logo]),
        ),
    ]
