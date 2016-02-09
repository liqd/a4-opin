# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('projects', '0008_auto_20160208_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link', models.URLField()),
                ('logo', models.ForeignKey(null=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='organisation',
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
    ]
