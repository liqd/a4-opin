# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160129_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdhocracyProjectPage',
            fields=[
                ('projectpage_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='projects.ProjectPage')),
                ('embedurl', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('projects.projectpage',),
        ),
    ]
