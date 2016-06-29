# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import euth.organisations.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('euth_organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=512, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('information', models.TextField(verbose_name=euth.organisations.models.Organisation)),
                ('is_public', models.BooleanField(default=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='projects/backgrounds', blank=True)),
                ('moderators', models.ManyToManyField(related_name='project_moderator', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(to='euth_organisations.Organisation')),
                ('participants', models.ManyToManyField(related_name='project_participant', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
