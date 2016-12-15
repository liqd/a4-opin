from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from jsonfield.fields import JSONField, JSONFormField


class GeoJSONValidator(object):

    def __init__(self, geom_type, required):
        self.geom_type = geom_type
        self.required = required

    def __call__(self, value):
        err_msg = None
        json_type = value.get('type')
        if json_type == 'Feature' and self.geom_type == 'GEOMETRY':
            geom_type = value.get('geometry').get('type')
            is_geometry = geom_type in (
                "Point", "MultiPoint", "LineString", "MultiLineString",
                "Polygon", "MultiPolygon", "GeometryCollection"
            )
            if not is_geometry:
                err_msg = '%s is not a valid GeoJSON geometry type' % geom_type
        elif json_type == 'FeatureCollection':
            if len(value.get('features')) == 0 and self.required:
                err_msg = 'Field can not be empty'

        if err_msg:
            raise ValidationError(err_msg)


class GeoJSONFormField(JSONFormField):

    def __init__(self, *args, **kwargs):
        geom_type = kwargs.pop('geom_type')
        required = kwargs.pop('required')
        kwargs.setdefault(
            'validators', [GeoJSONValidator(geom_type, required)])
        super(GeoJSONFormField, self).__init__(*args, **kwargs)


class GeoJSONField(JSONField):
    description = _("Geometry as GeoJSON")
    form_class = GeoJSONFormField
    dim = 2
    geom_type = 'GEOMETRY'

    def formfield(self, **kwargs):
        kwargs.setdefault('geom_type', self.geom_type)
        return super(GeoJSONField, self).formfield(**kwargs)


class GeometryField(GeoJSONField):
    pass


class PointField(GeometryField):
    geom_type = 'POINT'


class PolygonField(GeometryField):
    geom_type = 'POLYGON'


class MultiPolygonField(GeoJSONField):
    geom_type = 'MULTIPOLYGON'
