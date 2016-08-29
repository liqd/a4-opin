from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w_]+)/$', views.dispatch_project_view,
        name='project-detail'),
]
