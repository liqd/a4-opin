from django.utils import translation

class TranslatedField(object):
    def __init__(self, de_field, it_field, en_field, fr_field, sv_field, sl_field, da_field):
        self.de_field = de_field
        self.it_field = it_field
        self.en_field = en_field
        self.fr_field = fr_field
        self.sv_field = sv_field
        self.sl_field = sl_field
        self.da_field = da_field

    def __get__(self, instance, owner):
        de = getattr(instance, self.de_field)
        it = getattr(instance, self.it_field)
        en = getattr(instance, self.en_field)
        fr = getattr(instance, self.fr_field)
        sv = getattr(instance, self.sv_field)
        sl = getattr(instance, self.sl_field)
        da = getattr(instance, self.da_field)

        if translation.get_language() == 'de':
            return de
        elif translation.get_language() == 'it':
            return it
        elif translation.get_language() == 'fr':
            return fr
        elif translation.get_language() == 'sv':
            return sv
        elif translation.get_language() == 'sl':
            return sl
        elif translation.get_language() == 'da':
            return da
        else:
            return en
