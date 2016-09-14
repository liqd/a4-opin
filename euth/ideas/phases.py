from django.utils.translation import ugettext_lazy as _

from euth import phases

from . import apps, models, views


class CollectPhase(phases.PhaseContent):
    """
    Allows commenting and CRUD operations on ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'collect'
    weight = 20
    view = views.IdeaListView

    name = _('Collect phase')
    module_name = _('ideas collection')

    features = {
        'crud': (models.Idea,),
        'comment': (models.Idea,),
    }

phases.content.register(CollectPhase())


class RatingPhase(phases.PhaseContent):
    """
    Allows commenting and rating (aka voting) of ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'rating'
    weight = 30
    view = views.IdeaListView

    name = _('Rating phase')
    module_name = _('ideas collection')

    features = {
        'rating': (models.Idea,)
    }


phases.content.register(RatingPhase())


class CommentPhase(phases.PhaseContent):
    """
    Allows only commenting of ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'comment'
    weight = 40
    view = views.IdeaListView

    name = _('Comment phase')
    module_name = _('ideas collection')

    features = {
        'comment': (models.Idea,),
    }


phases.content.register(CommentPhase())


class UniversalPhase(phases.PhaseContent):
    """
    Allows all ideas operations. Emulates the old OPIN process.
    """
    app = apps.IdeaConfig.label
    phase = 'universal'
    weight = 50
    view = views.IdeaListView

    name = _('Universal phase')
    module_name = _('ideas collection')

    features = {
        'crud': (models.Idea,),
        'comment': (models.Idea,),
        'rating':  (models.Idea,),
    }


phases.content.register(UniversalPhase())
