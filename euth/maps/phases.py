from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps
from . import models
from . import views


class IssuePhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'issue'
    view = views.MapIdeaListView

    name = _('Issue Phase')
    description = _('Add, comment and rate new ideas on a map.')
    module_name = _('ideas collection')
    icon = 'far fa-map'

    features = {
        'crud': (models.MapIdea,),
        'comment': (models.MapIdea,),
        'rate': (models.MapIdea,),
    }


class CollectPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'collect'
    view = views.MapIdeaListView

    name = _('Collect Phase')
    description = _('Add and comment new ideas on a map.')
    module_name = _('ideas collection')
    icon = 'far fa-map'

    features = {
        'crud': (models.MapIdea,),
        'comment': (models.MapIdea,),
    }


class RatingPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'rating'
    view = views.MapIdeaListView

    name = _('Rating Phase')
    description = _('Get quantative feeback by rating the collected '
                    'ideas on a map.')
    module_name = _('ideas collection')
    icon = 'fas fa-chevron-up'

    features = {
        'rate': (models.MapIdea,),
    }


phases.content.register(IssuePhase())
phases.content.register(CollectPhase())
phases.content.register(RatingPhase())
