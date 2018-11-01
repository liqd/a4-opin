from django.utils.translation import ugettext_lazy as _

from adhocracy4 import phases

from . import apps, models, views


class CreateDocumentPhase(phases.PhaseContent):
    """
    Allows no interaction for participants, only
    creation for moderators.
    """
    app = apps.Config.label
    phase = 'create_document'
    view = views.DocumentCreateView

    name = _('Create document phase')
    module_name = _('commenting text')
    description = _('Create text for the project.')
    icon = 'file-text-o'

    features = {}


phases.content.register(CreateDocumentPhase())


class CommentPhase(phases.PhaseContent):
    """
    Allows only commenting of paragraphs.
    """
    app = apps.Config.label
    phase = 'comment'
    view = views.DocumentDetailView

    name = _('Comment phase')
    module_name = _('commenting text')
    description = _('Collect comments for the text.')
    icon = 'comment-o'

    features = {
        'comment': (models.Paragraph, models.Document),
    }


phases.content.register(CommentPhase())
