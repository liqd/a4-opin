from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.filters.filters import DistinctOrderingFilter
from adhocracy4.filters.filters import FreeTextFilter
from euth.contrib import filters as contrib_filters

from .models import Organisation

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('title', _('Alphabetical'))
]


class OrganisationFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'title'
    }

    search = FreeTextFilter(
        widget=contrib_filters.FreeTextSearchFilterWidget,
        fields=['name']
    )

    country = contrib_filters.CountryFilter()

    ordering = DistinctOrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('name', 'title'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=contrib_filters.OrderingFilterWidget
    )

    class Meta:
        model = Organisation
        fields = ['search', 'country', 'ordering']
