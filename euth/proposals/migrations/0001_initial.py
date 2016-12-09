# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0002_use-autoslug-filed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, to='euth_modules.Item', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description1', models.TextField()),
                ('description2', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_modules.item',),
        ),
    ]
