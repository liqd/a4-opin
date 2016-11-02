# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0006_add_helptext_and_verbose_name_to_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(verbose_name='Access to the project', help_text='Please indicate who should be able to participate in your project. Teasers for your project including title and short description will always be visible to everyone', default=True),
        ),
    ]
