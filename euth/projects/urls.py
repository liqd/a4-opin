from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^project-delete/(?P<pk>[-\w_]+)/$',
            views.ProjectDeleteView.as_view(),
            name='project-delete'),
    path('', views.ProjectListView.as_view(), name='project-list')
]
