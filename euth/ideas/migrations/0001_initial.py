# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('item_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='euth_modules.Item', parent_link=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('image', models.ImageField(validators=[euth.contrib.validators.validate_hero_image], blank=True, upload_to='ideas/images')),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_modules.item',),
        ),
    ]
