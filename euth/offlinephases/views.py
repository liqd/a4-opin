from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from adhocracy4.dashboard import mixins
from adhocracy4.projects.mixins import ProjectMixin

from . import forms as offlinephase_forms
from . import models as offlinephase_models


class OfflineEventDetailView(
    generic.DetailView
):
    model = offlinephase_models.OfflineEvent

    @property
    def project(self):
        return self.object.project


class OfflineEventListView(ProjectMixin,
                           mixins.DashboardBaseMixin,
                           mixins.DashboardComponentMixin,
                           generic.ListView):

    model = offlinephase_models.OfflineEvent
    template_name = 'euth_offlinephases/offlineevent_list.html'
    permission_required = 'a4projects.change_project'

    def get_queryset(self):
        return super().get_queryset().filter(project=self.project)

    def get_permission_object(self):
        return self.project


class OfflineEventCreateView(ProjectMixin,
                             mixins.DashboardBaseMixin,
                             mixins.DashboardComponentMixin,
                             mixins.DashboardComponentFormSignalMixin,
                             generic.CreateView):
    model = offlinephase_models.OfflineEvent
    form_class = offlinephase_forms.OfflineEventForm
    permission_required = 'a4projects.change_project'
    template_name = 'euth_offlinephases/offlineevent_create_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'a4dashboard:offlineevent-list',
            kwargs={'project_slug': self.project.slug})

    def get_permission_object(self):
        return self.project


class OfflineEventUpdateView(ProjectMixin,
                             mixins.DashboardBaseMixin,
                             mixins.DashboardComponentMixin,
                             mixins.DashboardComponentFormSignalMixin,
                             generic.UpdateView):
    model = offlinephase_models.OfflineEvent
    form_class = offlinephase_forms.OfflineEventForm
    permission_required = 'meinberlin_offlineevents.change_offlineevent'
    template_name = 'euth_offlinephases/offlineevent_create_form.html'
    get_context_from_object = True

    def get_success_url(self):
        return reverse(
            'a4dashboard:offlineevent-list',
            kwargs={'project_slug': self.project.slug})

    @property
    def organisation(self):
        return self.project.organisation

    def get_permission_object(self):
        return self.project


class OfflineEventDeleteView(ProjectMixin,
                             mixins.DashboardBaseMixin,
                             mixins.DashboardComponentMixin,
                             mixins.DashboardComponentDeleteSignalMixin,
                             generic.DeleteView):
    model = offlinephase_models.OfflineEvent
    success_message = _('The offline event has been deleted')
    permission_required = ''
    template_name = 'euth_offlinephases/offlineevent_confirm_delete.html'
    get_context_from_object = True

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse(
            'a4dashboard:offlineevent-list',
            kwargs={'project_slug': self.project.slug})

    @property
    def organisation(self):
        return self.project.organisation

    def get_permission_object(self):
        return self.project
