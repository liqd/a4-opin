from django.forms import widgets
from django.utils import formats
from django.utils.safestring import mark_safe


class DateInput(widgets.DateInput):

    class Media:
        js = (
            'flatpickr.js',
            'js/dateTimeInput.js',
        )
        css = {'all': (
            'flatpickr.css',
        )}

    input_type = 'text'
    format_index = 0

    def render(self, name, value, attrs=None, renderer=None):
        if attrs:
            format = formats.get_format(
                self.format_key
            )[self.format_index]
            attrs.update({
                'class': attrs.get('class', '') + ' flatpickr',
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
    }

    format_index = 0
    format_key = 'DATETIME_INPUT_FORMATS'
