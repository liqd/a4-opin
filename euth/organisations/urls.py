from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.OrganisationListView.as_view(), name='organisation-list'),
    re_path(r'^(?P<slug>[-\w_]+)/$',
            views.OrganisationDetailView.as_view(),
            name='organisation-detail'),
]
