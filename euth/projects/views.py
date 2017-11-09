

from adhocracy4.filters import views as filter_views
from adhocracy4.projects.models import Project

from . import filters


class ProjectListView(filter_views.FilteredListView):
    model = Project
    paginate_by = 12
    filter_set = filters.ProjectFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(is_draft=False)
