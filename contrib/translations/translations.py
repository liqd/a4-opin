from django.utils import translation
from wagtail.wagtailcore.blocks.stream_block import StreamValue

from euth_wagtail.settings import LANGUAGES


class TranslatedField(object):

    def __init__(self, field_name):
        for language_code, language in LANGUAGES:
            setattr(self, language_code + '_field', field_name + '_' + language_code)

    def has_content(self, field):
        if isinstance(field, StreamValue):
            value = field.stream_data
            if value:
                return True
            else:
                return False
        elif isinstance(field, str):
            if field:
                return True
            else:
                return False
        else:
            return False

    def __get__(self, instance, owner):
        lang = translation.get_language()
        value = getattr(instance, getattr(self, '{}_field'.format(lang)))

        if self.has_content(value):
            return value
        else:
            return getattr(instance, self.en_field)
