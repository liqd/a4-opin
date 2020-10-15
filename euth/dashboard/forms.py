
import parler
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from euth.organisations.models import Organisation


class OrganisationForm(forms.ModelForm):
    translated_fields = [
        ('description_why', forms.CharField, {
            'label': _('description why'),
            'widget': forms.Textarea,
        }),
        ('description_how', forms.CharField, {
            'widget': forms.Textarea,
            'label': _('description how')
        }),
        ('description', forms.CharField, {
            'label': _('description'),
            'help_text': _(
                'More info about the organisation / '
                'Short text for organisation overview'),
            'widget': forms.Textarea,
        })
    ]
    languages = [lang_code for lang_code, lang in settings.LANGUAGES]

    class Meta:
        model = Organisation
        fields = [
            'name', 'image', 'logo', 'twitter_handle', 'facebook_handle',
            'instagram_handle', 'webpage', 'country', 'place'
        ]
        help_texts = {
            'name': _('The title of your organisation'),
        }

    def _get_identifier(self, language, fieldname):
        return '{}__{}'.format(language, fieldname)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # inject additional form fields for translated model fields
        for lang_code in self.languages:
            for name, field_cls, kwargs in self.translated_fields:
                self.instance.set_current_language(lang_code)
                field = field_cls(**kwargs)
                identifier = self._get_identifier(
                    lang_code, name)
                field.required = False

                try:
                    translation = self.instance.get_translation(lang_code)
                    initial = getattr(translation, name)
                except parler.models.TranslationDoesNotExist:
                    initial = ''

                field.initial = initial
                self.fields[identifier] = field

    def translated(self):
        """
        Return translated fields as list of tuples (language code, fields).
        """

        from itertools import groupby
        fields = [(field.html_name.split('__')[0], field) for field in self
                  if '__' in field.html_name]
        groups = groupby(fields, lambda x: x[0])
        values = [(lang, list(map(lambda x: x[1], group)))
                  for lang, group in groups]
        return values

    def untranslated(self):
        """
        Return untranslated fields as flat list.
        """
        return [field for field in self if '__' not in field.html_name]

    def prefilled_languages(self):
        """
        Return languages tabs that need to be displayed.
        """
        languages = [lang for lang in self.languages
                     if lang in self.data
                     or self.instance.has_translation(lang)]
        return languages

    def get_initial_active_tab(self):
        active_languages = self.prefilled_languages()
        if len(active_languages) > 0:
            return active_languages[0]
        else:
            return 'en'

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit is True:
            for lang_code in self.languages:
                if lang_code in self.data:
                    instance.set_current_language(lang_code)
                    for fieldname, _cls, _kwargs in self.translated_fields:
                        identifier = '{}__{}'.format(lang_code, fieldname)
                        setattr(instance, fieldname,
                                self.cleaned_data.get(identifier))
                    instance.save()
                elif instance.has_translation(lang_code):
                    instance.delete_translation(lang_code)
        return instance

    def clean(self):
        for lang_code in self.languages:
            if lang_code in self.data:
                for fieldname in self.translated_fields:
                    identifier = self._get_identifier(lang_code, fieldname[0])
                    data = self.cleaned_data
                    if identifier not in data or not data[identifier]:
                        msg = 'This field is required'
                        raise ValidationError((identifier, msg))

        return self.cleaned_data
