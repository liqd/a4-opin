from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps
from . import models
from . import views


class IssuePhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'issue'
    view = views.IdeaListView

    name = _('Issue phase')
    description = _('Add new ideas.')
    module_name = _('ideas collection')
    icon = 'far fa-lightbulb'

    features = {
        'crud': (models.Idea,),
    }


class CollectPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'collect'
    view = views.IdeaListView

    name = _('Collect phase')
    description = _('Add new ideas and comment them.')
    module_name = _('ideas collection')
    icon = 'far fa-lightbulb'

    features = {
        'crud': (models.Idea,),
        'comment': (models.Idea,),
    }


class RatingPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'rating'
    view = views.IdeaListView

    name = _('Rating phase')
    module_name = _('ideas collection')
    description = _('Get quantative feeback by rating the collected ideas.')
    icon = 'fas fa-chevron-up'

    features = {
        'rate': (models.Idea,)
    }


class FeedbackPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'feedback'
    view = views.IdeaListView

    name = _('Feedback phase')
    description = _('Get feedback for collected ideas through rates and '
                    'comments.')
    module_name = _('ideas collection')
    icon = 'far fa-comment'

    features = {
        'rate': (models.Idea,),
        'comment': (models.Idea,)
    }


class UniversalPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = 'universal'
    view = views.IdeaListView

    name = _('Universal phase')
    module_name = _('ideas collection')
    description = _('Use all features of the idea collection.')
    icon = 'far fa-lightbulb'

    features = {
        'crud': (models.Idea,),
        'comment': (models.Idea,),
        'rate': (models.Idea,),
    }


phases.content.register(IssuePhase())
phases.content.register(CollectPhase())
phases.content.register(RatingPhase())
phases.content.register(FeedbackPhase())
phases.content.register(UniversalPhase())
