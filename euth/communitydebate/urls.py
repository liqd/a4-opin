from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.TopicCreateView.as_view(), name='topic-create'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.TopicUpdateView.as_view(), name='topic-update'),
    url(r'^(?P<slug>[-\w_]+)/delete/$',
        views.TopicDeleteView.as_view(), name='topic-delete'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.TopicDetailView.as_view(), name='topic-detail'),
]
