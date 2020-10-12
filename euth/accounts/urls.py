from django.conf.urls import include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.dashboard_default,
        name='account'),
    url(
        r'^profile/$',
        views.AccountProfileView.as_view(),
        name='account-profile'),
    url(
        r'^social/',
        include('allauth.socialaccount.urls')),
    url(
        r'',
        include('allauth.account.urls')),
]
