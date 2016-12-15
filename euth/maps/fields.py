from django.utils.translation import ugettext_lazy as _
from jsonfield.fields import JSONField, JSONFormField

from .validators import GeoJSONFormFieldValidator


class GeoJSONFormField(JSONFormField):

    def __init__(self, *args, **kwargs):
        geom_type = kwargs.pop('geom_type')
        required = kwargs.pop('required')
        kwargs.setdefault(
            'validators', [GeoJSONFormFieldValidator(geom_type, required)])
        super().__init__(*args, **kwargs)


class GeoJSONField(JSONField):
    description = _("Geometry as GeoJSON")
    form_class = GeoJSONFormField
    dim = 2
    geom_type = 'GEOMETRY'

    def __init__(self, *args, **kwargs):
        required = kwargs.pop('required', True)
        kwargs.setdefault(
            'validators', [GeoJSONFormFieldValidator(
                self.geom_type, required)])
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.setdefault('geom_type', self.geom_type)
        return super(GeoJSONField, self).formfield(**kwargs)

    def clean(self, *args, **kwargs):
        print(self.validators)
        super().clean(*args, **kwargs)


class GeometryField(GeoJSONField):
    pass


class PointField(GeometryField):
    geom_type = 'POINT'


class PolygonField(GeometryField):
    geom_type = 'POLYGON'


class MultiPolygonField(GeoJSONField):
    geom_type = 'MULTIPOLYGON'
