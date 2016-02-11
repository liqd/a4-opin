# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160211_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_da',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_de',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_en',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_fr',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_it',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sl',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sv',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_da',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_de',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_en',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_fr',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_it',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_sl',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_sv',
            field=models.TextField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='title_en',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
