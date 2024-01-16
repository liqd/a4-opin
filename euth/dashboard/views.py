from adhocracy4.dashboard.views import BlueprintListView
from adhocracy4.dashboard.views import ProjectCreateView
from adhocracy4.dashboard.views import ProjectListView
from adhocracy4.dashboard.views import ProjectPublishView


class ProjectAdminListView(ProjectListView):
    """Only admins can view dashboard"""

    permission_required = "euth_projects.add_project"


class ProjectAdminCreateView(ProjectCreateView):
    """Only admins can create new projects"""

    permission_required = "euth_projects.add_project"


class ProjectAdminPublishView(ProjectPublishView):
    """Only admins can publish new projects"""

    permission_required = "euth_projects.change_project"


class BlueprintAdminListView(BlueprintListView):
    """Only admins can view list of blueprints"""

    permission_required = "euth_projects.add_project"
