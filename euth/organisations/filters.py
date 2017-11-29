import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet, FreeTextFilter
from euth.contrib import filters as contrib_filters

from .models import Organisation

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('translations__title', _('Alphabetical'))
]


class OrganisationFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'translations__title'
    }

    search = FreeTextFilter(
        widget=contrib_filters.FreeTextSearchFilterWidget,
        fields=['translations__title']
    )

    country = contrib_filters.CountryFilter()

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('translations__title', 'title'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=contrib_filters.OrderingFilterWidget
    )

    class Meta:
        model = Organisation
        fields = ['search', 'country', 'ordering']
