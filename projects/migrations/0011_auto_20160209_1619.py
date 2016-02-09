# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160209_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectorganisations',
            name='page',
            field=modelcluster.fields.ParentalKey(to='projects.OrganisationPage', null=True, blank=True, related_name='organisation_projects'),
        ),
    ]
