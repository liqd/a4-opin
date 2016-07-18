from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$', login_required(views.IdeaCreateView.as_view()), name='idea-create'),
    url(r'^(?P<slug>[-\w_]+)/edit/$', views.IdeaUpdateView.as_view(), name='idea-update'),
    url(r'^(?P<slug>[-\w_]+)/$', views.IdeaDetailView.as_view(), name='idea-detail'),
]
