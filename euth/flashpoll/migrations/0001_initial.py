# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0002_use-autoslug-filed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashpoll',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='euth_modules.Item', serialize=False)),
                ('key', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_modules.item',),
        ),
    ]
