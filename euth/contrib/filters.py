import django_filters
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


class ArchivedFilter(django_filters.FilterSet):
    is_archived = django_filters.BooleanFilter(
                    name='archived',
                    widget=ArchivedFilterWidget
                )

    class Meta:
        model = models.Project
        fields = ['is_archived']
