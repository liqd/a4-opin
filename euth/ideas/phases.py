from euth.phases import content
from euth.phases.contents import PhaseContent

from . import views, apps


class CollectPhase(PhaseContent):
    app = apps.IdeaConfig.label
    phase = 'collect'
    view = views.IdeaListView
    weight = 20

content.register(CollectPhase())
