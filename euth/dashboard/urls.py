from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$',
        views.DashboardProfileView.as_view(),
        name='dashboard-profile'),
    url(r'^projects/$',
        views.DashboardProjectListView.as_view(),
        name='dashboard-project-list'),
    url(r'^projects/(?P<slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        name='dashboard-project-edit'),
    url(r'^$',
        views.DashboardOverviewView.as_view(),
        name='dashboard-overview'),
]
