from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$',
        views.OfflineEventDetailView.as_view(), name='offlineevent-detail'),
]
