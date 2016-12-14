# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashpoll',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('module', models.OneToOneField(related_name='settings', to='a4modules.Module')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
