from euth import phases

from . import apps, views


class BlogPhase(phases.PhaseContent):
    app = apps.BlogConfig.label
    phase = 'phase'
    view = views.PostDetail
    weight = 20

phases.content.register(BlogPhase())
