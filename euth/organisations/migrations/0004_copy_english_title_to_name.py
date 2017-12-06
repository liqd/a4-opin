# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def copyTitleToName(apps, schema_editor):
    Organisation = apps.get_model("euth_organisations", "organisation")
    db_alias = schema_editor.connection.alias

    for org in Organisation.objects.using(db_alias).all():
        name = org.translations.get(language_code='en').title
        # can not use save here because parler is not instanciated
        Organisation.objects.filter(pk=org.pk).update(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0003_change_image_and_logo'),
    ]

    operations = [
        migrations.RunPython(copyTitleToName)
    ]
