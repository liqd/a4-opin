# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20160211_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adhocracyprojectpage',
            name='adhocracySDK_url',
        ),
        migrations.RemoveField(
            model_name='adhocracyprojectpage',
            name='autoresize',
        ),
        migrations.RemoveField(
            model_name='adhocracyprojectpage',
            name='autourl',
        ),
        migrations.RemoveField(
            model_name='adhocracyprojectpage',
            name='embedurl',
        ),
        migrations.RemoveField(
            model_name='adhocracyprojectpage',
            name='height',
        ),
        migrations.AlterField(
            model_name='adhocracyprojectpage',
            name='locale',
            field=models.CharField(max_length=2, help_text='Leave blank to use the language that is set in the CMS', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_da',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_de',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_en',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_fr',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_it',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sl',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationpage',
            name='teaser_sv',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_da',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_de',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_en',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_fr',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_it',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_sl',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='teaser_sv',
            field=models.TextField(max_length=400, help_text='Max. 400 Characters', blank=True),
        ),
    ]
