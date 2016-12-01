from django.core.management.base import BaseCommand

from euth.actions import verbs
from euth.actions.models import Action
from euth.phases.models import Phase


class Command(BaseCommand):
    help = 'Notify users if a project which '
    'they follow ends within the next 24 hours'

    def handle(self, *args, **options):
        phases = Phase.objects.finish_next()

        for phase in phases:
            project = phase.module.project
            actions = Action.objects.filter(
                project=project,
                verb=verbs.COMPLETE,
            ).filter(
                timestamp__lt=phase.end_date
            ).filter(
                timestamp__gte=phase.start_date
            )

            if not actions:
                Action.objects.create(
                    project=project,
                    verb=verbs.COMPLETE
                )
