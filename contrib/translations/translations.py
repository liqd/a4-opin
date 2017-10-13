from django.db import models
from django.utils import translation
from wagtail.wagtailcore.blocks.stream_block import StreamValue
from wagtail.wagtailcore.models import PageBase

from euth_wagtail.settings import LANGUAGES

class TranslatedField(object):

    def __init__(self, field_name, field, overwrite_en_blank=None):
        for language_code, language in LANGUAGES:
            setattr(self, language_code + '_field', field_name + '_' + language_code)
        self.field_name = field_name
        self.field = field
        self.overwrite_en_blank = overwrite_en_blank

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
def _translated_attrs_from_field(value):
    translated_attrs = {}
    for lang_code, lang_name in LANGUAGES:
        field = value.field.clone()

        if lang_code == 'en' and value.overwrite_en_blank is not None:
            field.blank = value.overwrite_en_blank

        field_name = value.field_name + '_' + lang_code
        translated_attrs[field_name] = field
    return translated_attrs


class TranslatedModelMetaclass(models.base.ModelBase):
    """
    Add a real field for each TranslatedField and language.

    Scans the class upon creation for TranslatedFields and uses those to add
    real model fields to the model. The translated field can than be used as an
    accessor to the many generated fields.
    """


    def __new__(cls, name, bases, attrs):
        final_attrs = {}
        for attr in attrs.values():
            if isinstance(attr, TranslatedField):
                final_attrs.update(_translated_attrs_from_field(attr))

        final_attrs.update(attrs)
        return super().__new__(cls, name, bases, final_attrs)


class TranslatedPageMetaclass(TranslatedModelMetaclass, PageBase):
    pass


class TranslatedModel(models.Model, metaclass=TranslatedModelMetaclass):
    class Meta:
        abstract = True
