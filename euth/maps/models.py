from django.utils.translation import ugettext_lazy as _

from euth.ideas import models as idea_models
from euth.modules import models as module_models

from .fields import MultiPolygonField, PointField
from .widgets import MapChoosePolygonWidget


class AreaSettings(module_models.AbstractSettings):
    polygon = MultiPolygonField(required=True)

    def widgets(self):
        return {
            'polygon': MapChoosePolygonWidget
        }


class MapIdea(idea_models.Idea):
    point = PointField(
        verbose_name=_('Where can your idea be located on a map?'),
        help_text=_('Click inside marked area to set a marker. '
                    'Drag and drop marker to change place.'))

    objects = idea_models.IdeaQuerySet.as_manager()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('map-idea-detail', args=[str(self.slug)])
