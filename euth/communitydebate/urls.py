from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'create/module/(?P<slug>[-\w_]+)/$',
            views.TopicCreateView.as_view(), name='topic-create'),
    re_path(r'^(?P<slug>[-\w_]+)/edit/$',
            views.TopicUpdateView.as_view(), name='topic-update'),
    re_path(r'^(?P<slug>[-\w_]+)/delete/$',
            views.TopicDeleteView.as_view(), name='topic-delete'),
    re_path(r'^(?P<slug>[-\w_]+)/$',
            views.TopicDetailView.as_view(), name='topic-detail'),
]
