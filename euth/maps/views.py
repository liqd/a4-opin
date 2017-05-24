from euth.ideas import views as idea_views

from . import forms
from .models import MapIdea


class MapIdeaListView(idea_views.IdeaListView):
    model = MapIdea


class MapIdeaCreateView(idea_views.IdeaCreateView):
    model = MapIdea
    form_class = forms.MapIdeaForm
    permission_required = 'euth_maps.propose_mapidea'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['settings_instance'] = self.module.settings_instance
        return kwargs


class MapIdeaUpdateView(idea_views.IdeaUpdateView):
    model = MapIdea
    permission_required = 'euth_maps.modify_mapidea'
    form_class = forms.MapIdeaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['settings_instance'] = self.object.module.settings_instance
        return kwargs


class MapIdeaDeleteView(idea_views.IdeaDeleteView):
    model = MapIdea
    permission_required = 'euth_maps.modify_mapidea'


class MapIdeaDetailView(idea_views.IdeaDetailView):
    model = MapIdea
    permission_required = 'euth_maps.view_mapidea'
    queryset = MapIdea.objects\
                      .annotate_positive_rating_count()\
                      .annotate_negative_rating_count()
