from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import TextInput
from django.template import Context
from django.template.loader import get_template


class UserSearchInput(TextInput):
    class Media:
        js = (
            staticfiles_storage.url('typeahead.jquery.min.js'),
            staticfiles_storage.url('user_search.js'),
        )

    def __init__(self, identifier=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.identifier = identifier

    def render(self, name, value, attrs=None):
        if attrs and 'class' in attrs:
            attrs['class'] += ' typeahead'
        else:
            attrs['class'] = 'typeahead'

        if self.identifier:
            attrs['data-identifier'] = self.identifier

        input_field = super().render(name, value, attrs)

        template = get_template('euth_users/user_search.html')
        context = Context({
            'input': input_field,
        })

        return template.render(context)
