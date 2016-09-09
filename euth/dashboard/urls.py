from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$',
        views.DashboardProfileView.as_view(),
        name='dashboard-profile'),
    url(r'^projects/$',
        views.DashboardProjectListView.as_view(),
        name='dashboard-project-list'),
    url(r'^projects/create-overview$',
        views.DashboardCreateOverviewView.as_view(),
        name='dashboard-project-create-overview'),
    url(r'^projects/create/idea-collection$',
        views.DashboardCreateIdeaCollectionView.as_view(),
        name='dashboard-project-create-idea-collection'),
    url(r'^projects/create/commenting-text$',
        views.DashboardCreateCommentingTextView.as_view(),
        name='dashboard-project-create-commenting-text'),
    url(r'^projects/(?P<slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        name='dashboard-project-edit'),
    url(r'^projects/(?P<slug>[-\w_]+)/users$',
        views.DashboardProjectUserView.as_view(),
        name='dashboard-project-users'),
    url(r'^$',
        views.DashboardOverviewView.as_view(),
        name='dashboard-overview'),
]
