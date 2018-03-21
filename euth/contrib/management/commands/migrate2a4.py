import pytz
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.utils import DatabaseError


def with_timezone(date):
    if date:
        return date.replace(tzinfo=pytz.UTC)
    return date


class Command(BaseCommand):
    help = 'Migrate model objects or tables to adhocracy4 core'

    def add_arguments(self, parser):
        parser.add_argument('model', choices=['offlinephases'])
        parser.add_argument('--clear-target', action='store_true')
        parser.add_argument('--clear-source', action='store_true')

    def handle(self, *args, **options):
        model = options['model']
        if model == 'offlinephases':
            self._migrate_offlinephases(options['clear_target'],
                                        options['clear_source'])

    def _migrate_offlinephases(self, clear_target, clear_source):
        from adhocracy4.offlineevents.models import OfflineEvent
        from adhocracy4.offlineevents.models import OfflineEventDocument
        from adhocracy4.phases.models import Phase

        with connection.cursor() as cursor:
            offlinephases = {}
            offlineuploads = {}
            phases = {}
            try:
                cursor.execute('SELECT offlinephase_id, title, document, '
                               'created, modified '
                               'FROM euth_offlinephases_fileupload')
                for row in cursor.fetchall():
                    uploads = offlineuploads.get(row[0], [])
                    uploads.append(row)
                    offlineuploads[row[0]] = uploads

                cursor.execute('SELECT phase_id, text, created, modified '
                               'FROM euth_offlinephases_offlinephase')
                for row in cursor.fetchall():
                    offlinephases[row[0]] = row

            except DatabaseError as e:
                raise CommandError(
                    'Could not execute the query. '
                    'No problem if the following error says "no such table".\n'
                    '\tDatabaseError: ' + str(e)
                ) from e

            offlinephase_ids = offlinephases.keys()
            phases_set = Phase.objects.filter(id__in=offlinephase_ids)
            for phase in phases_set:
                phases[phase.id] = (phase.project,
                                    phase.name,
                                    phase.start_date)

            if clear_target:
                self.stdout.write('Clear target table: ' +
                                  OfflineEvent._meta.label)
                OfflineEvent.objects.all().delete()

            self.stdout.write('Copy from source table')

            for phase_id in offlinephase_ids:
                phase = phases[phase.id]
                offline = offlinephases[phase_id]
                uploads = offlineuploads[phase_id]

                event = OfflineEvent.objects.create(
                    project=phase[0],
                    name=phase[1],
                    date=phase[2],
                    description=offline[1],
                    created=with_timezone(offline[2]),
                    modified=with_timezone(offline[3])
                )
                self.stdout.write('Copied: ' + str(event))

                for upload in uploads:
                    document = OfflineEventDocument.objects.create(
                        offlineevent=event,
                        title=upload[1],
                        document=upload[2],
                        created=with_timezone(upload[3]),
                        modified=with_timezone(upload[4]),
                    )
                    self.stdout.write('Copied: ' + str(document))

            if clear_source:
                self.stdout.write('Clear source tables')
                phases_set.delete()
                cursor.execute('DROP TABLE euth_offlinephases_fileupload')
                cursor.execute('DROP TABLE euth_offlinephases_offlinephase')

        self.stdout.write('Done')
