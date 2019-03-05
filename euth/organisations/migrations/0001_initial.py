# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import parler.models
import django_countries.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, null=True, editable=False)),
                ('name', models.CharField(max_length=512, unique=True)),
                ('slug', models.SlugField(max_length=512, unique=True)),
                ('image', models.ImageField(upload_to='organisations/images', blank=True)),
                ('logo', models.ImageField(upload_to='organisations/logos', blank=True)),
                ('twitter_handle', models.CharField(max_length=200, blank=True)),
                ('facebook_handle', models.CharField(max_length=200, blank=True)),
                ('instagram_handle', models.CharField(max_length=200, blank=True)),
                ('webpage', models.URLField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('place', models.CharField(max_length=200)),
                ('initiators', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrganisationTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=512)),
                ('description_why', models.TextField()),
                ('description_how', models.TextField()),
                ('description', models.TextField()),
                ('master', models.ForeignKey(null=True, related_name='translations', editable=False, to='euth_organisations.Organisation', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'organisation Translation',
                'db_table': 'euth_organisations_organisation_translation',
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='organisationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
