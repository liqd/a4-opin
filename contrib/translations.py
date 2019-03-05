from django.db import models
from django.utils import translation
from wagtail.core.models import PageBase

from euth_wagtail.settings import LANGUAGES


class TranslatedField(object):
    fallback_lang = 'en'

    def __init__(self, field_name, field, overwrite_fallback={}):
        for language_code, language in LANGUAGES:
            setattr(self, language_code + '_field',
                    field_name + '_' + language_code)
        self.field_name = field_name
        self.field = field
        self.overwrite_fallback = overwrite_fallback

    def __get__(self, instance, owner):
        lang_code = translation.get_language()
        lang_field_name = self._get_translated_field_name(lang_code)
        value = getattr(instance, lang_field_name)

        if value:
            return value
        else:
            field_name = self._get_translated_field_name(self.fallback_lang)
            return getattr(instance, field_name)

    def _get_translated_field_name(self, lang_code):
        return '{}_{}'.format(self.field_name, lang_code)

    def _get_model_fields_spec(self):
        translated_attrs = {}
        for lang_code, lang_name in LANGUAGES:
            if lang_code == self.fallback_lang and self.overwrite_fallback:
                name, path, args, kwargs = self.field.deconstruct()
                kwargs.update(self.overwrite_fallback)
                field = self.field.__class__(*args, **kwargs)
            else:
                field = self.field.clone()

            field_name = self._get_translated_field_name(lang_code)
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
                final_attrs.update(attr._get_model_fields_spec())

        final_attrs.update(attrs)
        return super().__new__(cls, name, bases, final_attrs)


class TranslatedPageMetaclass(TranslatedModelMetaclass, PageBase):
    pass


class TranslatedModel(models.Model, metaclass=TranslatedModelMetaclass):
    class Meta:
        abstract = True
