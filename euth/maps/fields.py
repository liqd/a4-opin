from django.core import validators as django_validators
from django.utils.translation import ugettext_lazy as _
from jsonfield.fields import JSONField, JSONFormField

from .validators import GeoJSONFormFieldValidator


class GeoJSONFormField(JSONFormField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        empty_featureset = '{"type":"FeatureCollection","features":[]}'
        if (value not in django_validators.EMPTY_VALUES and not
                value == empty_featureset):
            return super().to_python(value)
        else:
            return None


class GeoJSONField(JSONField):
    description = _("Geometry as GeoJSON")
    form_class = GeoJSONFormField
    dim = 2
    geom_type = 'GEOMETRY'

    def formfield(self, **kwargs):
        return super(GeoJSONField, self).formfield(**kwargs)


class GeometryField(GeoJSONField):
    pass


class PointField(GeometryField):
    geom_type = 'POINT'


class MultiPolygonField(GeoJSONField):
    geom_type = 'MULTIPOLYGON'
