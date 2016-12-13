from django.views import generic
from .models import MapIdea


class MapIdeaListView(generic.ListView):
class MapIdeaCreateView(idea_views.IdeaCreateView):
    model = MapIdea
    form_class = forms.MapIdeaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['settings_instance'] = self.module.settings_instance
        return kwargs
    model = MapIdea
