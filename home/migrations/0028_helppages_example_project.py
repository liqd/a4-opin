# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_helppages'),
    ]

    operations = [
        migrations.AddField(
            model_name='helppages',
            name='example_project',
            field=models.URLField(null=True, help_text='Please enter project url.'),
        ),
    ]
