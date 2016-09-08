# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import euth.contrib.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('euth_organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(null=True, editable=False, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('information', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('image', models.ImageField(validators=[euth.contrib.validators.validate_hero_image], upload_to='projects/backgrounds', blank=True)),
                ('moderators', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='project_moderator')),
                ('organisation', models.ForeignKey(to='euth_organisations.Organisation')),
                ('participants', models.ManyToManyField(related_name='project_participant', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
