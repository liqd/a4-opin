from operator import itemgetter

import django_filters
from django.utils.translation import ugettext_lazy as _
from django_countries import Countries

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet, FreeTextFilter
from adhocracy4.projects.models import Project

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('name', _('Alphabetical'))
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


class ProjectFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest'
    }

    search = FreeTextFilter(
        widget=FreeTextSearchFilterWidget,
        fields=['name']
    )

    def organisation_countries(self, queryset, name, value):
        return queryset.filter(
            organisation__country=value
        )

    country = django_filters.CharFilter(
        name='',
        method='organisation_countries',
        widget=CountryFilterWidget,
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('name', 'title'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=OrderingFilterWidget
    )

    class Meta:
        model = Project
        fields = ['search', 'country', 'ordering']
