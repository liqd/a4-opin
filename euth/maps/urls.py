from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'create/module/(?P<slug>[-\w_]+)/$',
            views.MapIdeaCreateView.as_view(), name='map-idea-create'),
    re_path(r'^(?P<slug>[-\w_]+)/edit/$',
            views.MapIdeaUpdateView.as_view(), name='map-idea-update'),
    re_path(r'^(?P<slug>[-\w_]+)/delete/$',
            views.MapIdeaDeleteView.as_view(), name='map-idea-delete'),
    re_path(r'^(?P<slug>[-\w_]+)/$',
            views.MapIdeaDetailView.as_view(), name='map-idea-detail'),
]
