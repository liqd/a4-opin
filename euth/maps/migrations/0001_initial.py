# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import euth.maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0002_use-autoslug-filed'),
        ('euth_ideas', '0002_change_image_validator'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSettings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('polygon', euth.maps.fields.MultiPolygonField()),
                ('module', models.OneToOneField(to='euth_modules.Module', related_name='areasettings_settings')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MapIdea',
            fields=[
                ('idea_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='euth_ideas.Idea')),
                ('point', euth.maps.fields.PointField()),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_ideas.idea',),
        ),
    ]
