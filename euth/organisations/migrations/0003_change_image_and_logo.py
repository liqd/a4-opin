# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.images.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0002_use_adhocracy4_validators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('heroimage', help_prefix='The image sets the atmosphere for your organisation page.', blank=True, verbose_name='Header image', upload_to='organisations/images'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=adhocracy4.images.fields.ConfiguredImageField('logo', help_prefix='The official logo of your organisation.', upload_to='organisations/logos', blank=True),
        ),
    ]
