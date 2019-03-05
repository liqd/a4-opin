# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a4projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('target_object_id', models.CharField(null=True, blank=True, max_length=255)),
                ('action_object_object_id', models.CharField(null=True, blank=True, max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('public', models.BooleanField(db_index=True, default=True)),
                ('verb', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('action_object_content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', related_name='action_object', null=True, on_delete=models.CASCADE)),
                ('actor', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('project', models.ForeignKey(blank=True, to='a4projects.Project', null=True, on_delete=models.CASCADE)),
                ('target_content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', related_name='target', null=True, on_delete=models.CASCADE)),
            ],
        ),
    ]
