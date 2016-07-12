# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0003_organisation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=512)),
                ('description_why', models.TextField()),
                ('description_how', models.TextField()),
                ('description', models.TextField()),
                ('master', models.ForeignKey(editable=False, related_name='translations', null=True, to='euth_organisations.Organisation')),
            ],
            options={
                'managed': True,
                'verbose_name': 'organisation Translation',
                'db_tablespace': '',
                'db_table': 'euth_organisations_organisation_translation',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='organisationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
