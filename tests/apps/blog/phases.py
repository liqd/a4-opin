from adhocracy4 import phases

from . import apps, models, views


class BlogPhase(phases.PhaseContent):
    app = apps.BlogConfig.label
    phase = 'phase'
    view = views.PostList

    features = {
        'comment': (models.Post, )
    }


phases.content.register(BlogPhase())
