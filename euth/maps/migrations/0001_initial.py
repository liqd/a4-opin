# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adhocracy4.maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
        ('euth_ideas', '0002_change_image_validator'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSettings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('polygon', adhocracy4.maps.fields.MultiPolygonField()),
                ('module', models.OneToOneField(to='a4modules.Module', related_name='areasettings_settings', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MapIdea',
            fields=[
                ('idea_ptr', models.OneToOneField(serialize=False, auto_created=True, primary_key=True, parent_link=True, to='euth_ideas.Idea', on_delete=models.CASCADE)),
                ('point', adhocracy4.maps.fields.PointField()),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_ideas.idea',),
        ),
    ]
