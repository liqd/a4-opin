# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings

def forwards_func(apps, schema_editor):
    Organisation = apps.get_model('euth_organisations', 'Organisation')
    OrganisationTranslation = apps.get_model('euth_organisations', 'OrganisationTranslation')

    for object in Organisation.objects.all():
        OrganisationTranslation.objects.create(
            master_id=object.pk,
            language_code=settings.LANGUAGE_CODE,
            title=object.title,
            description_why=object.description_why,
            description_how=object.description_how,
            description=object.description
        )

def backwards_func(apps, schema_editor):
    Organisation = apps.get_model('euth_organisations', 'Organisation')
    OrganisationTranslation = apps.get_model('euth_organisations', 'OrganisationTranslation')

    for object in Organisation.objects.all():
        translation = _get_translation(object, OrganisationTranslation)
        object.title = translation.title
        object.description_why = translation.description_why
        object.description_how = translation.description_how
        object.description = translation.description
        object.save()

def _get_translation(object, OrganisatoinTranslation):
    translations = OrganisationTranslation.objects.filter(master_id=object.pk)
    try:
        # Try default translation
        return translations.get(language_code=settings.LANGUAGE_CODE)
    except ObjectDoesNotExist:
        try:
            # Try default language
            return translations.get(language_code=settings.PARLER_DEFAULT_LANGUAGE_CODE)
        except ObjectDoesNotExist:
            # Maybe the object was translated only in a specific language?
            # Hope there is a single translation
            return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0004_auto_20160711_1150'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
