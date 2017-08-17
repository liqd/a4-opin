from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models, views


class FlashpollPhase(phases.PhaseContent):
    app = apps.FlashpollConfig.label
    phase = 'poll'
    weight = 10
    view = views.FlashpollDetailView

    name = _('Flashpoll Phase')
    description = _('Initiate a Mobile polling process.')
    module_name = _('mobile polling')

    features = {
        'crud': (models.Flashpoll,),
    }

    icon = 'eject'


phases.content.register(FlashpollPhase())
