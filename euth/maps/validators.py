import json

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class GeoJSONFormFieldValidator(object):

    def __init__(self, geom_type, required):
        self.geom_type = geom_type
        self.required = required

    def __call__(self, value):
        if isinstance(value, str):
            value = json.loads(value)
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
                err_msg = _('Field can not be empty')

        if err_msg:
            raise ValidationError(err_msg)
