from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.ProjectDetailView.as_view(), name='project-detail'),
]
