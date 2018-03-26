from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.core.management.base import CommandError
from django.db import connection, models
from django.db.utils import DatabaseError
from django.utils import functional

from adhocracy4.comments import models as comment_models
from adhocracy4.models import base
from adhocracy4.offlineevents.models import OfflineEvent, OfflineEventDocument
from adhocracy4.phases import models as phase_models
from adhocracy4.phases.models import Phase


class LegacyOfflinephase(base.TimeStampedModel):
    text = RichTextUploadingField(blank=True, config_name='image-editor',)
    phase = models.OneToOneField(
        phase_models.Phase,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='+'
    )
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='+',
                               object_id_field='object_pk')

    @functional.cached_property
    def project(self):
        return self.phase.module.project

    class Meta:
        db_table = 'euth_offlinephases_offlinephase'


class LegacyFileUpload(base.TimeStampedModel):
    title = models.CharField(max_length=256)
    document = models.FileField()
    offlinephase = models.ForeignKey(LegacyOfflinephase,
                                     related_name='+')

    class Meta:
        db_table = 'euth_offlinephases_fileupload'


def migrate(cmd, clear_target, clear_source):

    if clear_target:
        cmd.stdout.write('Clear target table: ' +
                         OfflineEvent._meta.label)
        OfflineEvent.objects.all().delete()

    cmd.stdout.write('Copy from source tables')
    try:
        offlinephase_ids = []
        for offlinephase in LegacyOfflinephase.objects.all():
            offlinephase_ids.append(offlinephase.id)

            event = OfflineEvent.objects.create(
                name=offlinephase.phase.name,
                date=offlinephase.phase.start_date,
                description=offlinephase.text,
                project=offlinephase.phase.module.project,
                created=offlinephase.created,
                modified=offlinephase.modified
            )
            cmd.stdout.write('Copied: ' + str(event))

            for fileupload in LegacyFileUpload.objects.filter(
                    offlinephase_id=offlinephase.id):
                document = OfflineEventDocument.objects.create(
                    title=fileupload.title,
                    document=fileupload.document.file,
                    offlineevent=event
                )
                cmd.stdout.write('Copied: ' + str(document))

        if clear_source:
            cmd.stdout.write('Clear source tables and files')
            for fileupload in LegacyFileUpload.objects.all():
                fileupload.document.delete()
            Phase.objects.filter(id__in=offlinephase_ids).delete()
            with connection.cursor() as cursor:
                cursor.execute('DROP TABLE euth_offlinephases_fileupload')
                cursor.execute('DROP TABLE euth_offlinephases_offlinephase')

    except DatabaseError as e:
        raise CommandError(
            'Could not execute the query. '
            'No problem if the following error says "no such table".\n'
            '\tDatabaseError: ' + str(e)
        ) from e

    cmd.stdout.write('Done')
