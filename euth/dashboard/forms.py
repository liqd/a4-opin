import email.utils
import re

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from euth.contrib import widgets
from euth.memberships import models as member_models
from euth.organisations import models as org_models
from euth.phases import models as phase_models
from euth.projects import models as project_models
from euth.users import models as user_models

from . import multiform


class ProfileForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = ['avatar', 'email']
        widgets = {
            'avatar': widgets.ImageInputWidget()
        }


class ProjectInviteForm(forms.Form):
    emails = forms.CharField()

    def __init__(self, project, *args, **kwargs):
        self.project = project
        super().__init__(*args, **kwargs)

    def clean_emails(self):
        emails_str = self.cleaned_data['emails']
        emails = email.utils.getaddresses([emails_str])

        invalid_emails = []
        for name, email_addr in emails:
            if not re.match(r'^[^@]+@[^@\s]+\.[^@\s]+$', email_addr):
                invalid_emails.append(email_addr)
        if invalid_emails:
            message = '{} invalid email address'
            raise ValidationError(message.format(', '.join(invalid_emails)))

        addresses = [email[1] for email in emails]
        query = {
            'project': self.project,
            'email__in': addresses,
        }
        existing = member_models.Invite.objects.filter(**query)\
                                               .values_list('email', flat=True)
        if existing:
            for address in existing:
                raise ValidationError(
                    '{} already invited'.format(address)
                )

        return emails


class ProjectForm(forms.ModelForm):
    class Meta:
        model = project_models.Project
        fields = ['image', 'name', 'description', 'information', 'is_public',
                  'result']
        widgets = {
            'image': widgets.ImageInputWidget()
        }

    def save(self, commit=True):
        self.instance.is_draft = 'save_draft' in self.data
        return super().save(commit)


class PhaseForm(forms.ModelForm):
    class Meta:
        model = phase_models.Phase
        exclude = ('module', 'type')

        widgets = {
            'end_date': widgets.DateTimeInput(),
            'start_date': widgets.DateTimeInput(),
        }


class ProjectCompleteForm(multiform.MultiModelForm):
    base_forms = [
        ('project', ProjectForm),
        ('phases', modelformset_factory(
            phase_models.Phase, PhaseForm, extra=0
        )),
    ]


class RequestModerationForm(forms.ModelForm):
    ACTIONS = (
        ('accept', 'Accept'),
        ('decline', 'Decline'),
    )

    action = forms.ChoiceField(
        choices=ACTIONS,
        required=False,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = member_models.Request
        fields = ['action']


class InviteModerationForm(forms.ModelForm):
    delete = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = member_models.Request
        fields = ['delete']


class ParticipantsModerationForm(forms.ModelForm):
    delete = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = user_models.User
        fields = ['delete']


class ProjectUserForm(multiform.MultiModelForm):
    base_forms = [
        ('requests', forms.modelformset_factory(
            member_models.Request,
            RequestModerationForm,
            extra=0)),
        ('invites', forms.modelformset_factory(
            member_models.Invite,
            InviteModerationForm,
            extra=0)),
        ('users', forms.modelformset_factory(
            user_models.User,
            ParticipantsModerationForm,
            extra=0)),
    ]

    def __init__(self, *args, **kwargs):
        self.project = kwargs['project']
        del kwargs['project']
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            for form in self['requests'].forms:
                if form.cleaned_data['action'] == 'accept':
                    form.instance.accept()
                if form.cleaned_data['action'] == 'decline':
                    form.instance.decline()
            for form in self['invites'].forms:
                data = form.cleaned_data
                if 'delete' in data and data['delete']:
                    form.instance.delete()
            for form in self['users'].forms:
                data = form.cleaned_data
                if 'delete' in data and data['delete']:
                    self.project.participants.remove(form.instance)


class OrganisationForm(forms.ModelForm):
    """
    Special form that allows editing of all translated fields.
    """

    translated_fields = ['title', 'description',
                         'description_how', 'description_why']
    languages = [lang_code for lang_code, lang in settings.LANGUAGES]

    class Meta:
        model = org_models.Organisation
        fields = [
            'image', 'logo', 'twitter_handle', 'facebook_handle',
            'instagram_handle', 'webpage', 'country', 'place'
        ]
        widgets = {
            'image': widgets.ImageInputWidget(),
            'logo': widgets.ImageInputWidget(),
        }

    def _get_identifier(self, language, fieldname):
        return '{}__{}'.format(language, fieldname)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # inject additional form fields for translated model fields
        for lang_code in self.languages:
            for fieldname in self.translated_fields:
                self.instance.set_current_language(lang_code)
                label = fieldname.replace('_', ' ').capitalize()
                identifier = self._get_identifier(lang_code, fieldname)
                initial = self.instance.safe_translation_getter(fieldname)
                field = forms.CharField(label=label, max_length=400,
                                        required=False, initial=initial)
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

    def prefiled_languages(self):
        """
        Return languages tabs that need to be displayed.
        """
        languages = [lang for lang in self.languages
                     if lang in self.data
                     or self.instance.has_translation(lang)]
        # always provide english
        if 'en' not in languages:
            languages.insert(0, 'en')
        return languages

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit is True:
            for lang_code in self.languages:
                if lang_code in self.data:
                    instance.set_current_language(lang_code)
                    for fieldname in self.translated_fields:
                        identifier = '{}__{}'.format(lang_code, fieldname)
                        setattr(instance, fieldname,
                                self.cleaned_data.get(identifier))
                    instance.save()
        return instance

    def clean(self):
        for lang_code in self.languages:
            if lang_code in self.data:
                for fieldname in self.translated_fields:
                    identifier = self._get_identifier(lang_code, fieldname)
                    data = self.cleaned_data
                    if identifier not in data or not data[identifier]:
                        msg = 'This field is required'
                        raise ValidationError((identifier, msg))
        return self.cleaned_data
