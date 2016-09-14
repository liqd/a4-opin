from django.utils.translation import ugettext_lazy as _

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

    name = _('Comment phase')
    module_name = _('commenting text')

    features = {
        'comment': (models.Paragraph,),
    }


phases.content.register(CommentPhase())
