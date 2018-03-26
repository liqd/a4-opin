from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.management.base import CommandError
from django.db import connection, models
from django.db.utils import DatabaseError
from django.utils.translation import ugettext_lazy as _

from adhocracy4.models import base
from adhocracy4.offlineevents.models import OfflineEvent, OfflineEventDocument
from adhocracy4.projects import models as project_models


class LegacyOfflineEvent(base.TimeStampedModel):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120, verbose_name=_('Title'))
    date = models.DateTimeField(verbose_name=_('Date'))
    description = RichTextUploadingField(
        config_name='image-editor', verbose_name=_('Description'))
    project = models.ForeignKey(
        project_models.Project, on_delete=models.CASCADE, related_name='+')

    class Meta:
        db_table = 'euth_offlinephases_offlineevent'


class LegacyOfflineEventFileUpload(base.TimeStampedModel):
    title = models.CharField(max_length=256)
    document = models.FileField()
    offlineevent = models.ForeignKey(LegacyOfflineEvent, related_name='+')

    class Meta:
        db_table = 'euth_offlinephases_offlineeventfileupload'


def migrate(cmd, clear_target, clear_source):

    if clear_target:
        cmd.stdout.write('Clear target table: ' +
                         OfflineEvent._meta.label)
        OfflineEvent.objects.all().delete()

    cmd.stdout.write('Copy from source tables')
    try:
        for legacy_event in LegacyOfflineEvent.objects.all():
            event = OfflineEvent.objects.create(
                slug=legacy_event.slug,
                name=legacy_event.name,
                date=legacy_event.date,
                description=legacy_event.description,
                project_id=legacy_event.project_id,
                created=legacy_event.created,
                modified=legacy_event.modified
            )
            cmd.stdout.write('Copied: ' + str(event))

            for fileupload in LegacyOfflineEventFileUpload.objects.filter(
                    offlineevent_id=legacy_event.id).all():
                document = OfflineEventDocument.objects.create(
                    title=fileupload.title,
                    document=fileupload.document.file,
                    offlineevent=event
                )
                cmd.stdout.write('Copied: ' + str(document))

        if clear_source:
            cmd.stdout.write('Clear source tables and files')

            for fileupload in LegacyOfflineEventFileUpload.objects.all():
                fileupload.document.delete()

            with connection.cursor() as cursor:
                cursor.execute('DROP TABLE euth_offlinephases_offlineevent')
                cursor.execute(
                    'DROP TABLE euth_offlinephases_offlineeventfileupload')

    except DatabaseError as e:
        raise CommandError(
            'Could not execute the query. '
            'No problem if the following error says "no such table".\n'
            '\tDatabaseError: ' + str(e)
        ) from e

    cmd.stdout.write('Done')
