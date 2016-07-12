# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('euth_organisations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('information', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='projects/backgrounds')),
                ('moderators', models.ManyToManyField(related_name='project_moderator', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(to='euth_organisations.Organisation')),
                ('participants', models.ManyToManyField(blank=True, related_name='project_participant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
