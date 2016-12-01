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
        de = getattr(instance, self.de_field)
        it = getattr(instance, self.it_field)
        en = getattr(instance, self.en_field)
        fr = getattr(instance, self.fr_field)
        sv = getattr(instance, self.sv_field)
        sl = getattr(instance, self.sl_field)
        da = getattr(instance, self.da_field)

        if translation.get_language() == 'de' and self.has_content(de):
            return de
        elif translation.get_language() == 'it' and self.has_content(it):
            return it
        elif translation.get_language() == 'fr' and self.has_content(fr):
            return fr
        elif translation.get_language() == 'sv' and self.has_content(sv):
            return sv
        elif translation.get_language() == 'sl' and self.has_content(sl):
            return sl
        elif translation.get_language() == 'da' and self.has_content(da):
            return da
        else:
            return en
