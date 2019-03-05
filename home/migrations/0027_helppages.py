# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('home', '0026_add_subtitle_to_manuals_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpPages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('guidelines_page', models.ForeignKey(null=True, help_text='Please add a link to the guideline page.', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
