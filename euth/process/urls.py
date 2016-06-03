from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.listing, name='process-listing'),
    url(r'^(?P<process_name>\w+)/$', views.detail, name='process-detail'),
]
