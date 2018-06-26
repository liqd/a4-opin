from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, views


class FlashpollPhase(phases.PhaseContent):
    app = apps.FlashpollConfig.label
    phase = 'poll'
    view = views.FlashpollDetailView

    name = _('Flashpoll Phase')
    description = _('Initiate a Mobile polling process.')
    module_name = _('mobile polling')
    icon = 'times-circle-o'

    features = {
        # 'crud': (models.Flashpoll,),
    }


phases.content.register(FlashpollPhase())
