import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet, FreeTextFilter
from adhocracy4.projects.models import Project
from euth.organisations.models import Organisation

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('name', _('Alphabetical'))
]


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sorting')


class OrganisationFilterWidget(widgets.DropdownLinkWidget):
    label = _('Organisation')


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

    organisation = django_filters.ModelChoiceFilter(
        name='organisation__name',
        queryset=Organisation.objects.all(),
        widget=OrganisationFilterWidget,
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
        fields = ['search', 'organisation', 'ordering']
