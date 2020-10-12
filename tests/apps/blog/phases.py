from adhocracy4 import phases

from . import apps
from . import models
from . import views


class BlogPhase(phases.PhaseContent):
    app = apps.BlogConfig.label
    phase = 'phase'
    view = views.PostList

    features = {
        'comment': (models.Post, )
    }


phases.content.register(BlogPhase())
