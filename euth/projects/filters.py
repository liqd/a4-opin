from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.filters.filters import DistinctOrderingFilter
from adhocracy4.filters.filters import FreeTextFilter
from adhocracy4.projects.models import Project
from euth.contrib import filters as contrib_filters

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('name', _('Alphabetical'))
]


class ProjectFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest'
    }

    search = FreeTextFilter(
        widget=contrib_filters.FreeTextSearchFilterWidget,
        fields=['name']
    )

    country = contrib_filters.CountryFilter(
        field_name='organisation__country',
    )

    ordering = DistinctOrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('name', 'name'),
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=contrib_filters.OrderingFilterWidget
    )

    class Meta:
        model = Project
        fields = ['search', 'country', 'ordering']
