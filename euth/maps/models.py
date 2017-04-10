from django.db import models
from django.utils.translation import ugettext_lazy as _

from adhocracy4.modules import models as module_models
from euth.ideas import models as idea_models

from .fields import MultiPolygonField, PointField
from .widgets import MapChoosePolygonWidget


class AreaSettings(models.Model):
    module = models.OneToOneField(module_models.Module,
                                  on_delete=models.CASCADE,
                                  related_name='%(class)s_settings_legacy')
    polygon = MultiPolygonField()

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
