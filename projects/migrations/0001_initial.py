# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('logo', models.ForeignKey(related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, primary_key=True, to='wagtailcore.Page')),
                ('projecttype', models.CharField(max_length=255, choices=[('CT', 'Commenting Text'), ('IC', 'Idea Collection'), ('MP', 'Mobile Polling')])),
                ('title_en', models.CharField(max_length=255)),
                ('title_de', models.CharField(max_length=255, blank=True)),
                ('title_it', models.CharField(max_length=255, blank=True)),
                ('title_fr', models.CharField(max_length=255, blank=True)),
                ('title_sv', models.CharField(max_length=255, blank=True)),
                ('title_sl', models.CharField(max_length=255, blank=True)),
                ('title_da', models.CharField(max_length=255, blank=True)),
                ('teaser_en', models.CharField(max_length=255)),
                ('teaser_de', models.CharField(max_length=255, blank=True)),
                ('teaser_it', models.CharField(max_length=255, blank=True)),
                ('teaser_fr', models.CharField(max_length=255, blank=True)),
                ('teaser_sv', models.CharField(max_length=255, blank=True)),
                ('teaser_sl', models.CharField(max_length=255, blank=True)),
                ('teaser_da', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
