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
        {'dashboard_menu_item': 'profile'},
        name='dashboard-profile'),
    url(
        r'^email/$',
        views.DashboardEmailView.as_view(),
        {'dashboard_menu_item': 'email'},
        name='dashboard-email'
    ),
    url(
        r'^connections/$',
        views.DashboardAccountView.as_view(),
        {'dashboard_menu_item': 'connections'},
        name='dashboard-connections'
    ),
    url(
        r'^projects/$',
        views.DashboardUserProjectsView.as_view(),
        {'dashboard_menu_item': 'projects'},
        name='dashboard-user-projects'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/$',
        views.DashboardOrganisationUpdateView.as_view(),
        {'dashboard_menu_item': 'organisation'},
        name='dashboard-organisation-edit'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/$',
        views.DashboardProjectListView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-list'),
    url(r'^(?P<organisation_slug>[-\w_]+)/blueprints/$',
        views.DashboardBlueprintListView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-blueprint-list'),
    url(r'^(?P<organisation_slug>[-\w_]+)/blueprints/'
        r'(?P<blueprint_slug>[-\w_]+)/$',
        views.DashboardProjectCreateView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-create'),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-edit'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/delete$',
        views.DashboardProjectDeleteView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-delete'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/users$',
        views.DashboardProjectUserView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-users'
    ),
    url(
        r'^(?P<organisation_slug>[-\w_]+)/projects/'
        r'(?P<slug>[-\w_]+)/users/invite$',
        views.DashboardProjectInviteView.as_view(),
        {'dashboard_menu_item': 'project'},
        name='dashboard-project-invite'
    ),
]
