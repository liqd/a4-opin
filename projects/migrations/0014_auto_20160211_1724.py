# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_remove_organisationpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_da',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_de',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_en',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_fr',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_it',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sl',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sv',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
