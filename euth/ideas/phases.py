from euth import phases

from . import views, apps


class CollectPhase(phases.PhaseContent):
    app = apps.IdeaConfig.label
    phase = 'collect'
    view = views.IdeaListView
    weight = 20

phases.content.register(CollectPhase())
