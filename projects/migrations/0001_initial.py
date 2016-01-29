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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('logo', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('projecttype', models.CharField(max_length=255, choices=[('CT', 'Commenting Text'), ('IC', 'Idea Collection'), ('MP', 'Mobile Polling')])),
                ('title_en', models.CharField(max_length=255)),
                ('title_de', models.CharField(max_length=255, blank=True)),
                ('title_it', models.CharField(max_length=255, blank=True)),
                ('title_fr', models.CharField(max_length=255, blank=True)),
                ('title_sv', models.CharField(max_length=255, blank=True)),
                ('title_sl', models.CharField(max_length=255, blank=True)),
                ('title_da', models.CharField(max_length=255, blank=True)),
                ('teaser_en', models.TextField()),
                ('teaser_de', models.TextField(blank=True)),
                ('teaser_it', models.TextField(blank=True)),
                ('teaser_fr', models.TextField(blank=True)),
                ('teaser_sv', models.TextField(blank=True)),
                ('teaser_sl', models.TextField(blank=True)),
                ('teaser_da', models.TextField(blank=True)),
                ('image', models.ForeignKey(to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
                ('organisation', models.ForeignKey(to='projects.Organisation', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
