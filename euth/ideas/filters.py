import django_filters
from django.utils.translation import ugettext_lazy as _

from adhocracy4.categories import filters as cat_filters
from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet
from euth.ideas.models import Idea

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('comments', _('Most Comments')),
    ('support', _('Most Support'))
]


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sort by')


class IdeaFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest'
    }

    category = cat_filters.CategoryFilter()

    ordering = django_filters.OrderingFilter(
        fields=(
            ('-created', 'newest'),
            ('-comment_count', 'comments'),
            ('-positive_rating_count', 'support')
        ),
        choices=ORDERING_CHOICES,
        empty_label=None,
        widget=OrderingFilterWidget
    )

    class Meta:
        model = Idea
        fields = ['category', 'ordering']
