from django.utils import translation
from wagtail.wagtailcore.blocks.stream_block import StreamValue


class TranslatedField(object):

    def __init__(self, de_field, it_field, en_field, fr_field, sv_field, sl_field, da_field):
        self.de_field = de_field
        self.it_field = it_field
        self.en_field = en_field
        self.fr_field = fr_field
        self.sv_field = sv_field
        self.sl_field = sl_field
        self.da_field = da_field

    def hasContent(self, field):
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

        if translation.get_language() == 'de' and self.hasContent(de):
            return de
        elif translation.get_language() == 'it' and self.hasContent(it):
            return it
        elif translation.get_language() == 'fr' and self.hasContent(fr):
            return fr
        elif translation.get_language() == 'sv' and self.hasContent(sv):
            return sv
        elif translation.get_language() == 'sl' and self.hasContent(sl):
            return sl
        elif translation.get_language() == 'da' and self.hasContent(da):
            return da
        else:
            return en
