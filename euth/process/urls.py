from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.ProcessListView.as_view(), name='process-listing'),
    url(r'^(?P<process_slug>[-\w_]+)/$', views.ProcessDetailView.as_view(), name='process-detail'),
]
