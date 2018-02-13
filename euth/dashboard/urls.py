from django.conf.urls import url

from adhocracy4.dashboard.urls import urlpatterns as a4dashboard_urlpatterns
from euth.organisations.views import DashboardOrganisationUpdateView

app_name = 'a4dashboard'

urlpatterns = [
    url(r'^organisations/(?P<organisation_slug>[-\w_]+)/settings/$',
        DashboardOrganisationUpdateView.as_view(),
        name='organisation-edit')
] + a4dashboard_urlpatterns
