from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.dashboard import mixins
from adhocracy4.filters import views as filter_views
from adhocracy4.projects import models as prj_models
from adhocracy4.projects.mixins import ProjectMixin
from adhocracy4.projects.models import Project

from . import filters
from . import forms


class ProjectListView(filter_views.FilteredListView):
    model = Project
    paginate_by = 12
    filter_set = filters.ProjectFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(is_draft=False)


class ModeratorsDashboardView(
    ProjectMixin,
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    generic.detail.SingleObjectMixin,
    generic.FormView
):
    model = prj_models.Project
    fields = []
    permission_required = 'a4projects.change_project'
    project_url_kwarg = 'project_slug'
    template_name = 'euth_projects/dashboard_moderators.html'
    form_class = forms.AddModeratorForm

    def get_permission_object(self):
        return self.project

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.project


class ProjectDeleteView(PermissionRequiredMixin,
                        generic.DeleteView):
    model = prj_models.Project
    permission_required = 'a4projects.change_project'
    http_method_names = ['post']
    success_message = _("Project '%(name)s' was deleted successfully.")

    def get_success_url(self):
        return reverse_lazy('a4dashboard:project-list',
                            kwargs={
                                'organisation_slug':
                                    self.get_object().organisation.slug}
                            )

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
