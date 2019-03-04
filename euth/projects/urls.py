from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project-delete/(?P<pk>[-\w_]+)/$',
        views.ProjectDeleteView.as_view(),
        name='project-delete'),
    url(r'^$',
        views.ProjectListView.as_view(), name='project-list')
]
