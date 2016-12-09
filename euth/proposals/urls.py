from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        views.ProposalDetailView.as_view(), name='proposal-detail')
]
