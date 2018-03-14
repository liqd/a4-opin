from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from adhocracy4.dashboard import mixins as a4dashboard_mixins
from adhocracy4.filters import views as filter_views
from adhocracy4.projects import models as project_models
from euth.contrib import filters
from euth.dashboard import forms

from . import filters as organisation_filters
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
        return super().get_queryset().filter(organisation=self.organisation,
                                             is_draft=False)


class OrganisationDetailView(OrganisationMixin, filter_views.FilteredListView):
    model = project_models.Project
    filter_set = filters.ArchivedFilter
    template_name = 'euth_organisations/organisation_detail.html'


class OrganisationListView(filter_views.FilteredListView):
    model = models.Organisation
    paginate_by = 12
    filter_set = organisation_filters.OrganisationFilterSet


class DashboardOrganisationUpdateView(a4dashboard_mixins.DashboardBaseMixin,
                                      SuccessMessageMixin,
                                      generic.UpdateView):

    model = models.Organisation
    form_class = forms.OrganisationForm
    slug_url_kwarg = 'organisation_slug'
    template_name = 'euth_organisations/organisation_form.html'
    success_message = _('Organisation successfully updated.')
    permission_required = 'euth_organisations.modify_organisation'
    menu_item = 'organisation'

    def get_permission_object(self):
        return self.organisation
