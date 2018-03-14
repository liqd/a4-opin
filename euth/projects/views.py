from django.views import generic

from adhocracy4.dashboard import mixins
from adhocracy4.filters import views as filter_views
from adhocracy4.projects import models as prj_models
from adhocracy4.projects.mixins import ProjectMixin
from adhocracy4.projects.models import Project

from . import filters, forms


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
