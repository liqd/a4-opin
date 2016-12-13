from euth.ideas import models as idea_models
from euth.modules import models as module_models

from .fields import MultiPolygonField, PointField
from .widgets import MapChoosePolygonWidget


class AreaSettings(module_models.AbstractSettings):
    polygon = MultiPolygonField()

    def widgets(self):
        return {
            'polygon': MapChoosePolygonWidget
        }


class MapIdea(idea_models.Idea):
    point = PointField()

    objects = idea_models.IdeaQuerySet.as_manager()
