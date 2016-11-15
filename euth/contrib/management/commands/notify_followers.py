from django.core.management.base import BaseCommand

from euth.modules.models import Module
from euth.phases.models import Phase
from euth.projects.models import Project


class Command(BaseCommand):
    help = 'Notify users if a project which '
    'they follow ends within the next 24 hours'

    def handle(self, *args, **options):
        phases = Phase.objects.finish_next()
        modules_list = phases.values_list('module', flat=True)
        modules = Module.objects.filter(pk__in=modules_list)
        project_list = modules.values_list('project', flat=True)
        projects = Project.objects.filter(pk__in=project_list)
        print(projects)
