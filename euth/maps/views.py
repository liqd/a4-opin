from euth.ideas import views as idea_views

from . import forms
from .models import MapIdea


class MapIdeaListView(idea_views.IdeaListView):
    model = MapIdea


class MapIdeaCreateView(idea_views.IdeaCreateView):
    model = MapIdea
    form_class = forms.MapIdeaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['settings_instance'] = self.module.settings_instance
        return kwargs


class MapIdeaUpdateView(idea_views.IdeaUpdateView):
    model = MapIdea


class MapIdeaDeleteView(idea_views.IdeaDeleteView):
    model = MapIdea


class MapIdeaDetailView(idea_views.IdeaDetailView):
    model = MapIdea
