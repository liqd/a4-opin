from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'create/module/(?P<slug>[-\w_]+)/$',
            views.IdeaCreateView.as_view(), name='idea-create'),
    re_path(r'^(?P<slug>[-\w_]+)/edit/$',
            views.IdeaUpdateView.as_view(), name='idea-update'),
    re_path(r'^(?P<slug>[-\w_]+)/delete/$',
            views.IdeaDeleteView.as_view(), name='idea-delete'),
    re_path(r'^(?P<slug>[-\w_]+)/$',
            views.IdeaDetailView.as_view(), name='idea-detail'),
]
