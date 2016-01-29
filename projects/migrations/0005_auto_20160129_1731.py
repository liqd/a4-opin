# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projectspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='autoresize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='autourl',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='height',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='initial_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='locale',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='adhocracyprojectpage',
            name='widget',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='projecttype',
            field=models.CharField(choices=[('Commenting Text', 'Commenting Text'), ('Idea Collection', 'Idea Collection'), ('Mobile Polling', 'Mobile Polling')], max_length=255),
        ),
    ]
