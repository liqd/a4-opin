from django.urls import re_path

from adhocracy4.dashboard.urls import urlpatterns as a4dashboard_urlpatterns
from euth.dashboard import views
from euth.organisations.views import DashboardOrganisationUpdateView

app_name = 'a4dashboard'

urlpatterns = [
    re_path(r'^organisations/(?P<organisation_slug>[-\w_]+)/settings/$',
            DashboardOrganisationUpdateView.as_view(),
            name='organisation-edit'),
    re_path(
        r"^organisations/(?P<organisation_slug>[-\w_]+)/blueprints/$",
        views.BlueprintAdminListView.as_view(),
        name="blueprint-list",
    ),
    re_path(
        r"^organisations/(?P<organisation_slug>[-\w_]+)/projects/$",
        views.ProjectAdminListView.as_view(),
        name="project-list",
    ),
    re_path(
        r"^organisations/(?P<organisation_slug>[-\w_]+)/blueprints/"
        r"(?P<blueprint_slug>[-\w_]+)/$",
        views.ProjectAdminCreateView.as_view(),
        name="project-create",
    ),
    re_path(
        r"^publish/project/(?P<project_slug>[-\w_]+)/$",
        views.ProjectAdminPublishView.as_view(),
        name="project-publish",
    ),
] + a4dashboard_urlpatterns
