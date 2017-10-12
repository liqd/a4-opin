import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters import filters, widgets
from adhocracy4.projects import models


class ArchivedFilterWidget(widgets.DropdownLinkWidget):
    label = _('status')

    def __init__(self, attrs=None):
        choices = (
            ('false', _('active')),
            ('true', _('archived')),
            ('all', _('all'))
        )
        super().__init__(attrs, choices)


class ArchivedFilter(filters.DefaultsFilterSet):

    defaults = {
        'is_archived': 'false'
    }

    is_archived = django_filters.BooleanFilter(
                    name='is_archived',
                    widget=ArchivedFilterWidget
                )

    class Meta:
        model = models.Project
        fields = ['is_archived']
