from django.conf.urls import url

from . import views

_uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^activate/(?P<token>{})/$'.format(_uuid_pattern),
        views.activate_user,
        name='activate'),
    url(r'^reset/$', views.reset_request, name='reset_request'),
    url(r'^reset/(?P<token>{})/$'.format(_uuid_pattern),
        views.reset_password,
        name='reset_password'),

]
