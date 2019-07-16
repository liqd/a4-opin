from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^apply/(?P<project_slug>[-\w_]+)/$',
        views.RequestView.as_view(),
        name='memberships-request'
    ),

    url(
        r'^invites/(?P<invite_token>[-\w_]+)/$',
        views.InviteDetailView.as_view(),
        name='membership-invite-detail'
    ),
    url(
        r'^invites/(?P<invite_token>[-\w_]+)/accept/$',
        views.InviteUpdateView.as_view(),
        name='membership-invite-update'
    ),
]
