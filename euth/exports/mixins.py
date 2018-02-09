from django.utils.translation import ugettext as _

from adhocracy4.exports.views import VirtualFieldMixin


class ItemExportWithLocationMixin(VirtualFieldMixin):
    def get_virtual_fields(self, virtual):
        if 'location_lon' not in virtual:
            virtual['location_lon'] = _('Location (Longitude)')
        if 'location_lat' not in virtual:
            virtual['location_lat'] = _('Location (Latitude)')
        return super().get_virtual_fields(virtual)

    def get_location_lon_data(self, item):
        if hasattr(item, 'point'):
            point = item.point
            if 'geometry' in point:
                return point['geometry']['coordinates'][0]
        return ''

    def get_location_lat_data(self, item):
        if hasattr(item, 'point'):
            point = item.point
            if 'geometry' in point:
                return point['geometry']['coordinates'][1]
        return ''
