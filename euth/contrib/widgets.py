from datetime import datetime
from itertools import chain

import django_filters
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms import widgets
from django.forms.widgets import flatatt
from django.template.loader import render_to_string
from django.utils import formats
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.translation import get_language


class DateInput(widgets.DateInput):

    class Media:
        js = (staticfiles_storage.url('flatpickr.min.js'),
              staticfiles_storage.url('js/dateTimeInput.js'))
        css = {'all': [staticfiles_storage.url('flatpickr.min.css')]}

    input_type = 'text'
    format_index = 0

    # becomes a public value in Django 1.10
    def _format_value(self, value):
        format = formats.get_format(self.format_key)[self.format_index]
        if isinstance(value, str):
            date = datetime.strptime(value, format)
            return date.strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')
        else:
            return value.strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')

    def render(self, name, value, attrs=None):
        if attrs:
            format = formats.get_format(
                self.format_key
            )[self.format_index]
            attrs.update({
                'class': attrs.get('class', '') + ' flatpickr',
                'data-language': get_language(),
                'data-alt-format': format.replace('%', '').replace('M', 'i'),
                'data-date-format': format.replace('%', '').replace('M', 'i'),
            })

            if hasattr(self, 'additional_attrs'):
                attrs.update(self.additional_attrs)

            if value:
                attrs.update({
                    'data-default-date': self._format_value(value)
                })
        input = mark_safe(super().render(name, value, attrs))

        return input


class DateTimeInput(DateInput):

    additional_attrs = {
        'data-time_24hr': 'true',
        'data-enable-time': 'true',
        'data-alt-input': 'true'
    }

    format_index = 2
    format_key = 'DATETIME_INPUT_FORMATS'


class DropdownLinkWidget(django_filters.widgets.LinkWidget):
    label = None
    right = False
    template = 'euth_contrib/widgets/dropdown_link.html'

    def get_option_label(self, value, choices=()):
        option_label = BLANK_CHOICE_DASH[0][1]

        for v, label in chain(self.choices, choices):
            if str(v) == value:
                option_label = label
                break

        if option_label == BLANK_CHOICE_DASH[0][1]:
            option_label = _('All')

        return option_label

    def render(self, name, value, attrs=None, choices=()):
        all_choices = list(chain(self.choices, choices))

        if len(all_choices) <= 1:
            return ''

        if value is None:
            value = all_choices[0][0]

        _id = attrs.pop('id')
        final_attrs = flatatt(self.build_attrs(attrs))
        value_label = self.get_option_label(value, choices=choices)

        options = super().render(name, value, attrs={
            'class': 'dropdown-menu',
            'aria-labelledby': _id,
        }, choices=choices)

        return render_to_string(self.template, {
            'options': options,
            'id': _id,
            'attrs': final_attrs,
            'value_label': value_label,
            'label': self.label,
            'right': self.right,
        })
