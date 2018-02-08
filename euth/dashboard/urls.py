from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<organisation_slug>[-\w_]+)/$',
        views.DashboardOrganisationUpdateView.as_view(),
        name='dashboard-organisation-edit'
    ),
    url(
        r'^organisations/(?P<organisation_slug>[-\w_]+)/projects/$',
        views.DashboardProjectListView.as_view(),
        name='dashboard-project-list'),
    url(r'^organisations/(?P<organisation_slug>[-\w_]+)/blueprints/$',
        views.DashboardBlueprintListView.as_view(),
        name='dashboard-blueprint-list'),
    url(r'^organisations/(?P<organisation_slug>[-\w_]+)/blueprints/'
        r'(?P<blueprint_slug>[-\w_]+)/$',
        views.DashboardProjectCreateView.as_view(),
        name='dashboard-project-create'),
    url(
        r'^projects/(?P<project_slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        name='dashboard-project-edit'
    ),
    url(
        r'^projects/(?P<project_slug>[-\w_]+)/archive/$',
        views.DashboardProjectArchiveView.as_view(archiving=True),
        name='dashboard-project-archive'
    ),
    url(
        r'^projects/(?P<project_slug>[-\w_]+)/unarchive/$',
        views.DashboardProjectArchiveView.as_view(archiving=False),
        name='dashboard-project-unarchive',
    ),
    url(
        r'^projects/(?P<project_slug>[-\w_]+)/delete$',
        views.DashboardProjectDeleteView.as_view(),
        name='dashboard-project-delete'
    ),
    url(
        r'projects/(?P<project_slug>[-\w_]+)/users$',
        views.DashboardProjectUserView.as_view(),
        name='dashboard-project-users'
    ),
    url(
        r'^projects/(?P<project_slug>[-\w_]+)/users/invite$',
        views.DashboardProjectInviteView.as_view(),
        name='dashboard-project-invite'
    ),
]
