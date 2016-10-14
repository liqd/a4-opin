# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def shorten_phase_name_and_description(apps, schema_editor):
    Phase = apps.get_model('euth_phases', 'Phase')
    for phase in Phase.objects.all():
        phase.description = phase.description[:300]
        phase.name = phase.name[:80]
        phase.save()

class Migration(migrations.Migration):

    dependencies = [
        ('euth_phases', '0002_rename_comment_phase_to_feedback'),
    ]

    operations = [
        migrations.RunPython(shorten_phase_name_and_description)
    ]
