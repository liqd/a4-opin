from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'create/module/(?P<slug>[-\w_]+)/$',
        views.MapIdeaCreateView.as_view(), name='map-idea-create'),
    url(r'^(?P<slug>[-\w_]+)/edit/$',
        views.MapIdeaUpdateView.as_view(), name='map-idea-update'),
    url(r'^(?P<slug>[-\w_]+)/delete/$',
        views.MapIdeaDeleteView.as_view(), name='map-idea-delete'),
    url(r'^(?P<slug>[-\w_]+)/$',
        views.MapIdeaDetailView.as_view(), name='map-idea-detail'),
]
