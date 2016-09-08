from euth import phases

from . import apps, models, views


class CollectPhase(phases.PhaseContent):
    """
    Allows commenting and CRUD operations on ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'collect'
    view = views.IdeaListView
    weight = 20

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
    view = views.IdeaListView
    weight = 30

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
    view = views.IdeaListView
    weight = 40

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
    view = views.IdeaListView
    weight = 50

    features = {
        'crud': (models.Idea,),
        'comment': (models.Idea,),
        'rating':  (models.Idea,),
    }


phases.content.register(UniversalPhase())
