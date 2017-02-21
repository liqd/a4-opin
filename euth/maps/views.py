from django.conf import settings
from easy_thumbnails.files import get_thumbnailer

from euth.ideas import views as idea_views

from . import forms
from .models import MapIdea


class MapIdeaListView(idea_views.IdeaListView):
    model = MapIdea

    def dump_geojson(self):
        result = {}
        result['type'] = 'FeatureCollection'
        feature_list = []

        for item in self.get_queryset():

            url = ''

            if item.image:
                image = get_thumbnailer(item.image)['map_thumbnail']
                url = image.url

            properties = {
                'name': item.name,
                'slug': item.slug,
                'image':  url,
                'comments_count': item.comment_count,
                'positive_rating_count': item.positive_rating_count,
                'negative_rating_count': item.negative_rating_count,
                'url': item.get_absolute_url()
            }
            point_dict = item.point
            point_dict['properties'] = properties
            feature_list.append(point_dict)

        result['features'] = feature_list
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapideas_json'] = self.dump_geojson()
        context['map_url'] = settings.BASE_MAP
        context['polygon'] = self.module.settings_instance.polygon
        return context


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
    queryset = MapIdea.objects.annotate_positive_rating_count()\
        .annotate_negative_rating_count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_url'] = settings.BASE_MAP
        return context
