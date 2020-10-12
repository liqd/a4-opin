import django_filters
import pyuca
from django.utils.translation import ugettext_lazy as _
from django_countries import Countries

from adhocracy4.filters import filters
from adhocracy4.filters import widgets
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
        field_name='is_archived', widget=ArchivedFilterWidget)

    class Meta:
        model = models.Project
        fields = ['is_archived']


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sort by')


class SortedChoiceWidgetMixin:
    ignore_initial = None
    collator = pyuca.Collator()

    @property
    def choices(self):
        if not self._unsorted_choices:
            return None

        ignore_initial = self.ignore_initial or 0
        prefix = self._unsorted_choices[:ignore_initial]
        to_sort = self._unsorted_choices[ignore_initial:]

        return prefix + sorted(
            to_sort,
            key=lambda x: self.collator.sort_key(str(x[1]))
        )

    @choices.setter
    def choices(self, value):
        self._unsorted_choices = list(value)


class CountryFilterWidget(SortedChoiceWidgetMixin, widgets.DropdownLinkWidget):
    label = _('Country')
    ignore_initial = 1  # exclude all option from sort


class FreeTextSearchFilterWidget(widgets.FreeTextFilterWidget):
    label = _('Search')


class CountryFilter(django_filters.ChoiceFilter):

    def __init__(self, **kwargs):
        kwargs.setdefault('choices', list(Countries().countries.items()))
        kwargs.setdefault('widget', CountryFilterWidget)
        super().__init__(**kwargs)
