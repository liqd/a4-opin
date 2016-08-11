from euth import phases

from . import apps, views


class CollectPhase(phases.PhaseContent):
    """
    Allows commenting and CRUD operations on ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'collect'
    view = views.CollectPhaseView
    weight = 20

phases.content.register(CollectPhase())


class RatePhase(phases.PhaseContent):
    """
    Allows commenting and rating (aka voting) of ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'rate'
    view = views.RatePhaseView
    weight = 30

phases.content.register(RatePhase())


class CommentPhase(phases.PhaseContent):
    """
    Allows only commenting of ideas.
    """
    app = apps.IdeaConfig.label
    phase = 'comment'
    view = views.CommentPhaseView
    weight = 40

phases.content.register(CommentPhase())


class UniversalPhase(phases.PhaseContent):
    """
    Allows all ideas operations. Emulates the old OPIN process.
    """
    app = apps.IdeaConfig.label
    phase = 'universal'
    view = views.UniversalPhaseView
    weight = 50

phases.content.register(UniversalPhase())
