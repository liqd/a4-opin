from django.views import generic
from .models import MapIdea


class MapIdeaListView(generic.ListView):
    model = MapIdea
