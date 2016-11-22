from django.core.management.base import BaseCommand

from euth.actions.models import Action
from euth.phases.models import Phase
from euth.projects.models import Project


class Command(BaseCommand):
    help = 'Notify users if a project which '
    'they follow ends within the next 24 hours'

    def handle(self, *args, **options):
        phases = Phase.objects.finish_next()
        projects = Project.objects.filter(module__phase=phases)

        for project in projects:
            Action.objects.get_or_create(
                project=project,
                verb='project almost finished'
            )
