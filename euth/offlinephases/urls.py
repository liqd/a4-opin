from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/edit/$',
        views.OfflinephaseEditView.as_view(), name='offlinephase-edit'),
]
