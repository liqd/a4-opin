from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models, views


class DebatePhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'debate'
    view = views.TopicListView

    name = _('Debate phase')
    description = _('Add topics and debate them.')
    module_name = _('communitydebate')
    icon = 'far fa-comments'

    features = {
        'crud': (models.Topic,),
    }


phases.content.register(DebatePhase())
