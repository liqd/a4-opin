from django.urls import include
from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.dashboard_default,
        name='account'),
    path(
        'profile/',
        views.AccountProfileView.as_view(),
        name='account-profile'),
    path(
        'social/',
        include('allauth.socialaccount.urls')),
    path(
        '',
        include('allauth.account.urls')),
]
