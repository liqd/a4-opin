from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        r'^apply/(?P<project_slug>[-\w_]+)/$',
        views.RequestView.as_view(),
        name='memberships-request'
    ),

    re_path(
        r'^invites/(?P<invite_token>[-\w_]+)/$',
        views.InviteDetailView.as_view(),
        name='membership-invite-detail'
    ),
    re_path(
        r'^invites/(?P<invite_token>[-\w_]+)/accept/$',
        views.InviteUpdateView.as_view(),
        name='membership-invite-update'
    ),
]
