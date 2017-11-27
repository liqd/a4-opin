from operator import itemgetter

import django_filters
from django.utils.translation import ugettext_lazy as _
from django_countries import Countries

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet, FreeTextFilter
from . models import Organisation

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('translations__title', _('Alphabetical'))
]

COUNTRIES = list(Countries().countries.items())
COUNTRIES.sort(key=itemgetter(1))


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sort by')


class CountryFilterWidget(widgets.DropdownLinkWidget):
    label = _('Country')

    def __init__(self, attrs=None):
        choices = [('', _('All')), ]
        choices += COUNTRIES
        super().__init__(attrs, choices)


class FreeTextSearchFilterWidget(widgets.FreeTextFilterWidget):
    label = _('Search')


class OrganisationFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'translations__title'
    }

    search = FreeTextFilter(
        widget=FreeTextSearchFilterWidget,
        fields=['translations__title']
    )

    def countries(self, queryset, name, value):
        return queryset.filter(
            country=value
        )

    country = django_filters.CharFilter(
        name='',
        method='countries',
        widget=CountryFilterWidget,
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('translations__title', 'title'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=OrderingFilterWidget
    )

    class Meta:
        model = Organisation
        fields = ['search', 'country', 'ordering']
