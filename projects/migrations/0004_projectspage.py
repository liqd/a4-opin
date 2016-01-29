# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('projects', '0003_adhocracyprojectpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('title_de', models.CharField(blank=True, max_length=255)),
                ('title_it', models.CharField(blank=True, max_length=255)),
                ('title_fr', models.CharField(blank=True, max_length=255)),
                ('title_sv', models.CharField(blank=True, max_length=255)),
                ('title_sl', models.CharField(blank=True, max_length=255)),
                ('title_da', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
