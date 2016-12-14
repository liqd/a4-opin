from django.core.management.base import BaseCommand

from adhocracy4.phases.models import Phase
from euth.actions import verbs
from euth.actions.models import Action


class Command(BaseCommand):
    help = 'Notify users if a project which '
    'they follow ends within the next 24 hours'

    def handle(self, *args, **options):
        phases = Phase.objects.finish_next()

        for phase in phases:
            project = phase.module.project
            existing_action = Action.objects.filter(
                project=project,
                verb=verbs.COMPLETE,
                timestamp=phase.end_date,
            )

            if not existing_action:
                Action.objects.create(
                    project=project,
                    verb=verbs.COMPLETE,
                    timestamp=phase.end_date,
                    target=phase,
                )
