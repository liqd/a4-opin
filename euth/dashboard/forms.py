import collections
import re

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models import loading
from django.forms import modelformset_factory
from django.utils.translation import ugettext as _

from adhocracy4.modules import models as module_models
from adhocracy4.phases import models as phase_models
from adhocracy4.projects import models as project_models
from contrib.multiforms import multiform
from euth.contrib import widgets
from euth.memberships import models as member_models
from euth.offlinephases.models import Offlinephase
from euth.organisations import models as org_models
from euth.users import models as user_models


class ProfileForm(forms.ModelForm):

    class Meta:
        model = user_models.User
        fields = ['username', '_avatar', 'description', 'birthdate',
                  'country', 'city', 'gender', 'languages', 'twitter_handle',
                  'facebook_handle', 'instagram_handle', 'get_notifications']
        widgets = {
            'description': forms.Textarea(),
            'birthdate': widgets.DateInput(),
        }

    @property
    def formsections(self):
        formsections = collections.OrderedDict([
            (_('Basic Info'), [
                'username',
                '_avatar',
            ]),
            (_('Personal Info'), [
                'description',
                'birthdate',
                'country',
                'city',
                'gender',
            ]),
            (_('Ways to connect with you'), [
                'languages',
                'twitter_handle',
                'facebook_handle',
                'instagram_handle',
            ]),
            (_('Notifications'), [
                'get_notifications',
            ])
        ])

        return formsections


class ProjectInviteForm(forms.Form):
    emails = forms.CharField(
        label=_('E-mail addresses of invited users'),
        help_text=_('Enter the e-mail addresses of users who you want '
                    'to invite, separated by commas. Invited users will get '
                    'an email to confirm their membership in the project.'),
        widget=forms.TextInput(attrs={
            'placeholder': 'magdalena@example.com, yves@example.com,'
                           ' nadine@example.com…'}
        ),
        validators=[RegexValidator(
            # a list of emails, separated by commas with optional space after
            regex=r'^([^@]+@[^@\s]+\.[^@\s,]+((,\s?)|$))+$',
            message=_('Please enter correct e-mail addresses, separated by '
                      'commas.')
        )]
    )

    def __init__(self, project, *args, **kwargs):
        self.project = project
        super().__init__(*args, **kwargs)

    def clean_emails(self):
        emails_str = self.cleaned_data['emails'].strip(' ,')
        emails = re.split(r',\s?', emails_str)

        query = {
            'project': self.project,
            'email__in': emails,
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
        fields = ['name', 'description', 'image', 'information', 'is_public',
                  'result']

    def save(self, commit=True):
        self.instance.is_draft = 'save_draft' in self.data
        return super().save(commit)

    def get_checkbox_label(self, name):
        checkbox_labels = {
            'is_public': _('Accessible to all registered users of OPIN.me')
        }
        if name in checkbox_labels:
            return checkbox_labels[name]
        else:
            return ''

    @property
    def formsections(self):
        formsections = {}
        information_section = collections.OrderedDict([
            (_('Project settings'), [
                'name',
                'description',
                'image',
                'is_public'
            ]),
            (_('Information for your participants'), [
                'information'
            ])
        ])
        formsections['information'] = information_section
        return formsections


class PhaseForm(forms.ModelForm):
    delete = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = phase_models.Phase
        exclude = ('module', )

        widgets = {
            'end_date': widgets.DateTimeInput(),
            'start_date': widgets.DateTimeInput(),
            'type': forms.HiddenInput(),
            'weight': forms.HiddenInput()
        }


def get_module_settings_form(settings_instance_or_modelref):
    if hasattr(settings_instance_or_modelref, 'module'):
        settings_model = settings_instance_or_modelref.__class__
    else:
        settings_model = loading.get_model(
            settings_instance_or_modelref[0],
            settings_instance_or_modelref[1],
        )

    class ModuleSettings(forms.ModelForm):

        class Meta:
            model = settings_model
            exclude = ['module']
            widgets = settings_model().widgets()

    return ModuleSettings


class ProjectUpdateForm(multiform.MultiModelForm):

    def __init__(self, *args, **kwargs):
        qs = kwargs['phases__queryset']
        module = qs.first().module
        self.base_forms = [
            ('project', ProjectForm),
            ('phases', modelformset_factory(
                phase_models.Phase, PhaseForm, extra=0
            )),
        ]

        if module.settings_instance:
            self.base_forms.append((
                'module_settings',
                get_module_settings_form(module.settings_instance),
            ))

        super().__init__(*args, **kwargs)

    def save(self, commit=True):

        objects = super().save(commit=False)
        project = objects['project']

        if commit:
            project.save()
            if 'module_settings' in objects:
                objects['module_settings'].save()

        module = project.module_set.first()

        cleaned_data = self._combine('cleaned_data', call=False,
                                     call_kwargs={'commit': commit})
        phases = cleaned_data['phases']

        for phase in phases:
            delete = phase['delete']
            del phase['delete']
            if phase['id']:
                phase_object = phase['id']
                del phase['id']
                if not delete:
                    for key in phase:
                        value = phase[key]
                        setattr(phase_object, key, value)
                    if commit:
                        phase_object.save()
                else:
                    if commit:
                        phase_object.delete()
            else:
                if not delete:
                    del phase['id']
                    new_phase = phase_models.Phase(**phase)
                    new_phase.module = module
                    if commit:
                        new_phase.save()
                        if new_phase.type.startswith('euth_offlinephases'):
                            Offlinephase.objects.get_or_create(phase=new_phase)


class ProjectCreateForm(multiform.MultiModelForm):

    def __init__(self, blueprint, organisation, creator, *args, **kwargs):
        kwargs['phases__queryset'] = phase_models.Phase.objects.none()
        kwargs['phases__initial'] = [
            {'phase_content': t,
             'type': t.identifier,
             'weight': index
             } for index, t in enumerate(blueprint.content)
        ]

        self.organisation = organisation
        self.blueprint = blueprint
        self.creator = creator

        self.base_forms = [
            ('project', ProjectForm),
            ('phases', modelformset_factory(
                phase_models.Phase, PhaseForm,
                min_num=len(blueprint.content),
                max_num=len(blueprint.content),
            )),
        ]

        module_settings = blueprint.settings_model
        if module_settings:
            self.base_forms.append((
                'module_settings',
                get_module_settings_form(module_settings),
            ))

        return super().__init__(*args, **kwargs)

    def save(self, commit=True):
        objects = super().save(commit=False)

        project = objects['project']
        project.organisation = self.organisation
        if commit:
            project.save()
            project.moderators.add(self.creator)

        module = module_models.Module(
            name=project.slug + '_module',
            weight=1,
            project=project
        )
        objects['module'] = module
        if commit:
            module.save()

        if 'module_settings' in objects.keys():
            module_settings = objects['module_settings']
            module_settings.module = module
            if commit:
                module_settings.save()

        phases = objects['phases']

        for index, phase in enumerate(phases):
            phase.module = module
            if commit:
                phase.save()
                if phase.type.startswith('euth_offlinephases'):
                    Offlinephase.objects.create(phase=phase)

        return objects


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

    translated_fields = [('title', forms.CharField(
        help_text=_(
            'The title of '
            'your organisation'))),
        ('description_why', forms.CharField(
            widget=forms.Textarea)),
        ('description_how', forms.CharField(
            widget=forms.Textarea)),
        ('description', forms.CharField(
            widget=forms.Textarea, help_text=_(
                'More info about the organisation / '
                'Short text for organisation overview')))]
    languages = [lang_code for lang_code, lang in settings.LANGUAGES]

    class Meta:
        model = org_models.Organisation
        fields = [
            'image', 'logo', 'twitter_handle', 'facebook_handle',
            'instagram_handle', 'webpage', 'country', 'place'
        ]

    def _get_identifier(self, language, fieldname):
        return '{}__{}'.format(language, fieldname)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # inject additional form fields for translated model fields
        for lang_code in self.languages:
            for name, translated_field in self.translated_fields:
                self.instance.set_current_language(lang_code)
                label = name.replace('_', ' ').capitalize()
                identifier = self._get_identifier(
                    lang_code, name)
                initial = self.instance.safe_translation_getter(
                    name)
                field = translated_field
                field.label = label
                field.required = False
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
                        identifier = '{}__{}'.format(lang_code, fieldname[0])
                        setattr(instance, fieldname[0],
                                self.cleaned_data.get(identifier))
                    instance.save()
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
