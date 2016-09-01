from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^apply/(?P<project_slug>[-\w_]+)/$',
        views.RequestView.as_view(),
        name='memberships-request'
    ),
 ]
