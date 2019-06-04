from django.utils.translation import ugettext_lazy as _

from adhocracy4.maps import fields as map_fields
from euth.ideas import models as idea_models


class MapIdea(idea_models.Idea):
    point = map_fields.PointField(
        verbose_name=_('Where can your idea be located on a map?'),
        help_text=_('Click inside marked area to set a marker. '
                    'Drag and drop marker to change place.'))

    objects = idea_models.IdeaQuerySet.as_manager()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('map-idea-detail', args=[str(self.slug)])
