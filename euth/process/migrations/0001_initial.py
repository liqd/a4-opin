# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField(null=True, blank=True)),
                ('date_end', models.DateTimeField(null=True, blank=True)),
                ('module', models.ForeignKey(to='process.ParticipationModule')),
            ],
        ),
        migrations.CreateModel(
            name='PhaseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField(db_index=True)),
                ('moderator_permissions', models.ManyToManyField(to='auth.Permission', related_name='moderator_permissions')),
                ('module_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('participant_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=512)),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('moderators', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='process_moderator')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='process_participant', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='phase_type',
            field=models.ForeignKey(to='process.PhaseType'),
        ),
        migrations.AddField(
            model_name='participationmodule',
            name='process',
            field=models.ForeignKey(to='process.Process'),
        ),
        migrations.AlterUniqueTogether(
            name='phasetype',
            unique_together=set([('module_type', 'name'), ('module_type', 'order')]),
        ),
        migrations.AlterUniqueTogether(
            name='phase',
            unique_together=set([('phase_type', 'module')]),
        ),
        migrations.AlterUniqueTogether(
            name='participationmodule',
            unique_together=set([('process', 'order')]),
        ),
    ]
