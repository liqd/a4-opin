from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w_]+)/$', views.RequestsProjectDetailView.as_view(),
        name='project-detail'),
]
