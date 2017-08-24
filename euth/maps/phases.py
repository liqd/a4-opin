from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models, views


class IssuePhase(phases.PhaseContent):
    app = apps.MapConfig.label
    phase = 'issue'
    weight = 10
    view = views.MapIdeaListView

    name = _('Issue Phase')
    description = _('Add, comment and rate new ideas on a map.')
    module_name = _('ideas collection')
    icon = 'map-o'

    features = {
        'crud': (models.MapIdea,),
        'comment': (models.MapIdea,),
        'rate': (models.MapIdea,),
    }


class CollectPhase(phases.PhaseContent):
    app = apps.MapConfig.label
    phase = 'collect'
    weight = 20
    view = views.MapIdeaListView

    name = _('Collect Phase')
    description = _('Add and comment new ideas on a map.')
    module_name = _('ideas collection')
    icon = 'map-o'

    features = {
        'crud': (models.MapIdea,),
        'comment': (models.MapIdea,),
    }


class RatingPhase(phases.PhaseContent):
    app = apps.MapConfig.label
    phase = 'rating'
    weight = 30
    view = views.MapIdeaListView

    name = _('Rating Phase')
    description = _('Get quantative feeback by rating the collected '
                    'ideas on a map.')
    module_name = _('ideas collection')
    icon = 'chevron-up'

    features = {
        'rate': (models.MapIdea,),
    }


phases.content.register(IssuePhase())
phases.content.register(CollectPhase())
phases.content.register(RatingPhase())
