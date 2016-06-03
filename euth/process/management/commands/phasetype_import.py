from importlib import import_module
from importlib.util import find_spec
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission

from ...models import PhaseType


class Command(BaseCommand):
    help = 'Import all phase types'

    def handle(self, *args, **kwargs):
        for app in settings.INSTALLED_APPS:
            app_phases = app + ".phases"
            if find_spec(app_phases) is None:
                continue

            module = import_module(app_phases)

            if not hasattr(module, "available_phases"):
                continue

            for phase_name, phase in module.available_phases.items():
                print(
                    "From app `{}` importing `{}` phase type".format(
                        app, phase))

                moderator_permissions = [Permission.objects.get(codename=p)
                                         for p in phase["permissions"]["moderator"]]

                participant_permissions = [Permission.objects.get(codename=p)
                                           for p in phase["permissions"]["participant"]]

                phase_type, created = PhaseType.objects.update_or_create(
                    app_label=app,
                    name=phase_name)

                phase_type.moderator_permissions.add(*moderator_permissions)
                phase_type.participant_permissions.add(
                    *participant_permissions)
