from euth import phases

from . import apps, models, views


class CommentPhase(phases.PhaseContent):

    """
    Allows only commenting of paragraphs.
    """
    app = apps.DocumentConfig.label
    phase = 'comment'
    view = views.DocumentDetailView
    weight = 40

    features = {
        'comment': (models.Paragraph,),
    }


phases.content.register(CommentPhase())
