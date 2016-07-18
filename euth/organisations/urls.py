from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OrganisationListView.as_view(), name='organisation-list'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.OrganisationDetailView.as_view(), name='organisation-detail'),
]
