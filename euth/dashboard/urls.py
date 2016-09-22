from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.dashboard,
        name='dashboard'),
    url(
        r'^profile$',
        views.DashboardProfileView.as_view(),
        name='dashboard-profile'),
    url(
        r'^email/$',
        views.DashboardEmailView.as_view(),
        name='dashboard-email'
    ),
    url(
        r'^connections/$',
        views.DashboardAccountView.as_view(),
        name='dashboard-connections'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/$',
        views.DashboardOrganisationUpdateView.as_view(),
        name='dashboard-organisation-edit'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/$',
        views.DashboardProjectListView.as_view(),
        name='dashboard-project-list'),
    url(r'^(?P<organisation_slug>[-\w_]+)/blueprints/$',
        views.DashboardBlueprintListView.as_view(),
        name='dashboard-blueprint-list'),
    url(r'^(?P<organisation_slug>[-\w_]+)/blueprints/'
        r'(?P<blueprint_slug>[-\w_]+)/$',
        views.DashboardProjectCreateView.as_view(),
        name='dashboard-project-create'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        name='dashboard-project-edit'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/users$',
        views.DashboardProjectUserView.as_view(),
        name='dashboard-project-users'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/'
        r'(?P<slug>[-\w_]+)/users/invite$',
        views.DashboardProjectInviteView.as_view(),
        name='dashboard-project-invite'
    ),
]
