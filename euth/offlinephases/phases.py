from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models


class OfflinePhase(phases.PhaseContent):
    app = apps.OfflinephaseConfig.label
    phase = 'offline'
    weight = 0
    view = ''

    name = _('Offlinephase')
    description = _('Add documentation for Offlineevents.')
    module_name = _('offlinephase')

    features = {
        'crud': (models.Offlinephase,),
    }

phases.content.register(OfflinePhase())
