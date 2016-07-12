# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='modules.Item', serialize=False)),
                ('slug', models.SlugField(max_length=512, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('image', models.ImageField(validators=[euth.contrib.validators.validate_hero_image], upload_to='ideas/images', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('modules.item',),
        ),
    ]
