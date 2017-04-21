from django.shortcuts import get_object_or_404
from django.views import generic

from adhocracy4.filters import views as filter_views
from adhocracy4.projects import models as project_models
from euth.contrib import filters

from . import models


class OrganisationMixin():
    def dispatch(self, request, *args, **kwargs):
        slug = kwargs['slug']
        self.organisation = get_object_or_404(models.Organisation, slug=slug)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organisation'] = self.organisation
        return context

    def get_queryset(self):
        return super().get_queryset().filter(organisation=self.organisation)


class OrganisationDetailView(OrganisationMixin, filter_views.FilteredListView):
    model = project_models.Project
    filter_set = filters.ArchivedFilter
    template_name = 'euth_organisations/organisation_detail.html'


class OrganisationListView(generic.ListView):
    model = models.Organisation
    paginate_by = 12
