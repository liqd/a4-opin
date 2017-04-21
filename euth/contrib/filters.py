import django_filters
from django.http import QueryDict
from django.utils.translation import ugettext as _

from adhocracy4.projects import models

from . import widgets


class ArchivedFilterWidget(widgets.DropdownLinkWidget):
    label = _("Archived")

    def __init__(self, attrs=None):
        choices = (
            ('false', _('No')),
            ('true', _('Yes'))
        )
        super().__init__(attrs, choices)


class DefaultsFilterSet(django_filters.FilterSet):

    def __init__(self, query_data, *args, **kwargs):
        data = QueryDict(mutable=True)
        data.update(self.defaults)
        data.update(query_data)
        super().__init__(data, *args, **kwargs)


class ArchivedFilter(DefaultsFilterSet):

    defaults = {
        'is_archived': 'false'
    }

    is_archived = django_filters.BooleanFilter(
                    name='archived',
                    widget=ArchivedFilterWidget
                )

    class Meta:
        model = models.Project
        fields = ['is_archived']
