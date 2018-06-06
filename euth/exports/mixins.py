from django.core.exceptions import ObjectDoesNotExist
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


class ItemExportWithRepliesToMixin(VirtualFieldMixin):
    def get_virtual_fields(self, virtual):
        virtual['replies_to'] = _('replies to')
        return super().get_virtual_fields(virtual)

    def get_replies_to_data(self, comment):
        try:
            return comment.parent_comment.get().pk
        except ObjectDoesNotExist:
            return ''


class UserGeneratedContentExportMixin(VirtualFieldMixin):
    def get_virtual_fields(self, virtual):
        if 'creator' not in virtual:
            virtual['creator'] = _('Creator')
        if 'created' not in virtual:
            virtual['created'] = _('Created')
        return super().get_virtual_fields(virtual)

    def get_creator_data(self, item):
        return item.creator.username

    def get_created_data(self, item):
        return item.created.isoformat()
