# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def euth_to_a4_areasettings(apps, schema_editor):
    SourceAreas = apps.get_model('euth_maps', 'AreaSettings')
    TargetAreas = apps.get_model('a4maps', 'AreaSettings')
    copy_areasettings(SourceAreas, TargetAreas)


def a4_to_euth_areasettings(apps, schema_editor):
    SourceAreas = apps.get_model('a4maps', 'AreaSettings')
    TargetAreas = apps.get_model('euth_maps', 'AreaSettings')
    copy_areasettings(SourceAreas, TargetAreas)


def copy_areasettings(SourceAreas, TargetAreas):
    for area in SourceAreas.objects.all():
        TargetAreas.objects.update_or_create(
            module=area.module,
            defaults={
                'polygon': area.polygon
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('euth_maps', '0003_prepare_deprecation_of_areasettings'),
        ('a4maps', '0001_initial')
    ]

    operations = [
        migrations.RunPython(
            euth_to_a4_areasettings,
            a4_to_euth_areasettings
        )
    ]
