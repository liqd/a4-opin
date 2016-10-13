from django.utils.translation import ugettext_lazy as _

from euth import phases

from . import apps, models, views


class CreateDocumentPhase(phases.PhaseContent):

    """
    Allows only commenting of paragraphs.
    """
    app = apps.DocumentConfig.label
    phase = 'create_document'
    view = views.DocumentCreateView
    weight = 30

    name = _('Create document phase')
    module_name = _('commenting text')
    description = _('Create text for the project.')

    features = {
        'comment': (models.Paragraph,),
    }


phases.content.register(CreateDocumentPhase())


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
    description = _('Collect comments for the text.')

    features = {
        'comment': (models.Paragraph,),
    }


phases.content.register(CommentPhase())
