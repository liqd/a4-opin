# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0003_replace_modelutils'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, serialize=False, to='euth_modules.Item', parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_modules.item',),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, null=True, editable=False)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('text', ckeditor.fields.RichTextField()),
                ('weight', models.PositiveIntegerField()),
                ('document', models.ForeignKey(to='euth_documents.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
