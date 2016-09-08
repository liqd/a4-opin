# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(editable=False, null=True, blank=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=512)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('description', models.TextField(null=True, blank=True)),
                ('weight', models.PositiveIntegerField()),
                ('project', models.ForeignKey(to='euth_projects.Project')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='module',
            field=models.ForeignKey(to='euth_modules.Module'),
        ),
    ]
