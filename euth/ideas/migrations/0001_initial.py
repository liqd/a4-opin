# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('item_ptr', models.OneToOneField(to='a4modules.Item', parent_link=True, serialize=False, auto_created=True, primary_key=True, on_delete=models.CASCADE)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('name', models.CharField(max_length=120)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='ideas/images', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('a4modules.item',),
        ),
    ]
