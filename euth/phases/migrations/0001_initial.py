# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('permissions', models.CharField(max_length=128)),
                ('module', models.ForeignKey(to='modules.Module')),
            ],
        ),
    ]
