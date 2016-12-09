from django.utils.translation import ugettext_lazy as _

from euth import phases

from . import apps, models, views


class IssuePhase(phases.PhaseContent):
    app = apps.ProposalConfig.label
    phase = 'issue'
    weight = 10
    view = views.ProposalListView

    name = _('Issue phase')
    description = _('Add new proposals.')
    module_name = _('proposal collection')

    features = {
        'crud': (models.Proposal,),
    }
phases.content.register(IssuePhase())


class FeedbackPhase(phases.PhaseContent):
    app = apps.ProposalConfig.label
    phase = 'feedback'
    weight = 40
    view = views.ProposalListView

    name = _('Feedback phase')
    description = _('Get feedback for collected proposals through rates and '
                    'comments.')
    module_name = _('proposal collection')

    features = {
        'rate': (models.Proposal,),
        'comment': (models.Proposal,)
    }
phases.content.register(FeedbackPhase())
