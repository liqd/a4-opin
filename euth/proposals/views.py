from django.views import generic

from euth.projects import mixins

from .models import Proposal


class ProposalDetailView(generic.DetailView):
    model = Proposal


class ProposalListView(mixins.ProjectMixin, generic.ListView):
    model = Proposal
