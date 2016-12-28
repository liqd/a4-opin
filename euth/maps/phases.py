from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models, views


class IssuePhase(phases.PhaseContent):
    app = apps.MapConfig.label
    phase = 'issue'
    weight = 10
    view = views.MapIdeaListView

    name = _('Issue Phase')
    description = _('Add new ideas.')
    module_name = _('ideas collection')

    features = {
        'crud': (models.MapIdea,),
        'comment': (models.MapIdea,),
        'rate': (models.MapIdea,),
    }

phases.content.register(IssuePhase())
