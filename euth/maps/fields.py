from django.core import validators as django_validators
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

    def to_python(self, value):
        if value not in django_validators.EMPTY_VALUES:
            return super().to_python(value)
        else:
            return None


class GeoJSONField(JSONField):
    description = _("Geometry as GeoJSON")
    form_class = GeoJSONFormField
    dim = 2
    geom_type = 'GEOMETRY'

    '''
    def __init__(self, *args, **kwargs):
        required = kwargs.pop('required', True)
        kwargs.setdefault(
            'validators', [GeoJSONFormFieldValidator(
                self.geom_type, required)])
        super().__init__(*args, **kwargs)
    '''

    def formfield(self, **kwargs):
        kwargs.setdefault('geom_type', self.geom_type)
        return super(GeoJSONField, self).formfield(**kwargs)


class GeometryField(GeoJSONField):
    pass


class PointField(GeometryField):
    geom_type = 'POINT'


class MultiPolygonField(GeoJSONField):
    geom_type = 'MULTIPOLYGON'
