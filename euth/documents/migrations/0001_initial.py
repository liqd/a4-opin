# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('a4modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='a4modules.Item', serialize=False, parent_link=True, on_delete=models.CASCADE)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
            bases=('a4modules.item',),
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, null=True, editable=False)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('text', ckeditor.fields.RichTextField()),
                ('weight', models.PositiveIntegerField()),
                ('document', models.ForeignKey(to='euth_documents.Document', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
