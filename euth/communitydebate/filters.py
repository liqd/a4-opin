from django.utils.translation import ugettext_lazy as _

from adhocracy4.categories import filters as cat_filters
from adhocracy4.filters import widgets
from adhocracy4.filters.filters import DefaultsFilterSet
from adhocracy4.filters.filters import DistinctOrderingFilter

from .models import Topic

ORDERING_CHOICES = [
    ('newest', _('Most Recent')),
    ('comments', _('Most Comments')),
    ('support', _('Most Support'))
]


class OrderingFilterWidget(widgets.DropdownLinkWidget):
    label = _('Sort by')


class TopicFilterSet(DefaultsFilterSet):

    defaults = {
        'ordering': 'newest'
    }

    category = cat_filters.CategoryFilter()

    ordering = DistinctOrderingFilter(
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
        model = Topic
        fields = ['category', 'ordering']
