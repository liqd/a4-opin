import django_filters
from django.http import QueryDict
from django.utils.translation import ugettext_lazy as _

from adhocracy4.categories import models as category_models
from adhocracy4.projects import models

from . import widgets


class ArchivedFilterWidget(widgets.DropdownLinkWidget):
    label = _('status')

    def __init__(self, attrs=None):
        choices = (
            ('false', _('active')),
            ('true', _('archived')),
            ('all', _('all'))
        )
        super().__init__(attrs, choices)


class DefaultsFilterSet(django_filters.FilterSet):

    def __init__(self, query_data, *args, **kwargs):
        data = QueryDict(mutable=True)
        data.update(self.defaults)
        data.update(query_data)
        super().__init__(data, *args, **kwargs)


class ArchivedFilter(DefaultsFilterSet):

    defaults = {
        'is_archived': 'false'
    }

    is_archived = django_filters.BooleanFilter(
                    name='is_archived',
                    widget=ArchivedFilterWidget
                )

    class Meta:
        model = models.Project
        fields = ['is_archived']


def category_queryset(request):
    return category_models.Category.objects.filter(
        module=request.module)


class CategoryFilterWidget(widgets.DropdownLinkWidget):
    label = _('Category')


class CategoryFilter(django_filters.ModelChoiceFilter):

    def __init__(self, *args, **kwargs):
        if 'queryset' not in kwargs:
            kwargs['queryset'] = category_queryset
        if 'widget' not in kwargs:
            kwargs['widget'] = CategoryFilterWidget
        super().__init__(*args, **kwargs)
