# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20160209_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlashpollProjectPage',
            fields=[
                ('projectpage_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, serialize=False, to='projects.ProjectPage')),
                ('embedurl', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('projects.projectpage',),
        ),
    ]
