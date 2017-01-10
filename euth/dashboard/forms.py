import collections
import email.utils
import re
import json
import time
import datetime
import requests
import uuid

from requests.auth import HTTPBasicAuth
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import loading
from django.forms import modelformset_factory
from django.utils.translation import ugettext as _

from adhocracy4.modules import models as module_models
from adhocracy4.phases import models as phase_models
from adhocracy4.projects import models as project_models
from contrib.multiforms import multiform
from euth.contrib import widgets
from euth.memberships import models as member_models
from euth.organisations import models as org_models
from euth.users import models as user_models


class ProfileForm(forms.ModelForm):

    class Meta:
        model = user_models.User
        fields = ['username', '_avatar', 'description', 'birthdate',
                  'country', 'city', 'gender', 'languages', 'twitter_handle',
                  'facebook_handle', 'instagram_handle', 'get_notifications']
        widgets = {
            '_avatar': widgets.ImageInputWidget(),
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
        )
    )

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
        fields = ['name', 'description', 'image', 'information', 'is_public',
                  'result']
        widgets = {
            'image': widgets.ImageInputWidget()
        }

    def save(self, commit=True):
	
        print("save:"+ json.dumps(self.data))
        
        if 'save_draft' in self.data and self.data['current_preview']=='True':
            #Handling unpublish		
            url_poll = '{base_url}/poll/{poll_id}/opin/stop'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=self.data['module_settings-key']
            )
            print("url_poll:"+ url_poll)
            # Handle delete
            headers = {'Content-type': 'application/json'}        
            response = requests.delete(url_poll, headers=headers, auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER, settings.FLASHPOLL_BACK_PASSWORD))
            print ("code:"+str(response.status_code))
            print ("headers:"+ str(response.headers))
            print ("content:"+ str(response.text))              
        else:            

            startTime = time.mktime(datetime.datetime.strptime(self.data['startTime'], "%d/%m/%Y %H:%M").timetuple())
            endTime = time.mktime(datetime.datetime.strptime(self.data['endTime'], "%d/%m/%Y %H:%M").timetuple())

            jsonGenerator = {}
            print("json:"+ json.dumps(jsonGenerator))
            jsonGenerator['title'] = self.data['title']
            print("json:"+ json.dumps(jsonGenerator))
            jsonGenerator['shortDescription'] = self.data['shortDescription']
            print("json:"+ json.dumps(jsonGenerator))
            jsonGenerator['longDescription'] = self.data['longDescription']
            jsonGenerator['concludeMessage'] = self.data['concludeMessage']
            jsonGenerator['descriptionMediaURLs'] = [""]
            jsonGenerator['keywords'] = []
            jsonGenerator['startTime'] = startTime
            jsonGenerator['endTime'] = endTime
            jsonGenerator['resultVisibility'] = 0        
            jsonGenerator['preview'] = not 'save_draft' in self.data


            # context
            jsonGenerator['lab'] = 'opin'
            jsonGenerator['domain'] = 'opin'
            jsonGenerator['campaign'] = 'default'		

            # location
            jsonGenerator['geofenceLocation'] = self.data['geofenceLocation']
            jsonGenerator['geofenceRadius'] = 0
            jsonGenerator['geofenceId'] = ''

            # questions
            q = 1
            questions = []
            question_key = "question-"+str(q)+".questionType"
            while  question_key in self.data:
                question = {}
                question['questionText'] = self.data["question-"+str(q)+".questionText"]
                question['orderId'] = q
                question['questionType'] = self.data["question-"+str(q)+".questionType"]

                if "question-"+str(q)+".mandatory" in self.data:
                    question['mandatory'] = True
                else:
                    question['mandatory'] = False

        
                
                question['mediaURLs'] = [""]

                # answers
                a = 1
                answers = []
                answer_key = "question-"+str(q)+".choice-"+str(a)+".answerText"
                while  answer_key in self.data:
                    answer = {}
                    print("question-"+str(q)+".choice-"+str(a)+".answerText")
                    answer['answerText'] = self.data["question-"+str(q)+".choice-"+str(a)+".answerText"]
                    answer['orderId'] = a
                    answer['mediaURL'] = ''
                    if self.data["question-"+str(q)+".questionType"] == "FREETEXT":
                        answer['freetextAnswer'] = True
                    else:
                        answer['freetextAnswer'] = False

                    answers.append(answer)
                    a=a+1
                    answer_key = "question-"+str(q)+".choice-"+str(a)+".answerText"

                question['answers'] = answers
                questions.append(question)
                q=q+1
                question_key = "question-"+str(q)+".questionType"


            jsonGenerator['questions'] = questions
            json_data = json.dumps(jsonGenerator)
            print("json:"+ json.dumps(jsonGenerator))

            url_poll = '{base_url}/poll/{poll_id}/opin'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=self.data['module_settings-key']
            )

            print("url_poll:"+ url_poll)

            # Handle post
            headers = {'Content-type': 'application/json'}
            response = requests.post(url_poll, data=json_data, headers=headers, auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER, settings.FLASHPOLL_BACK_PASSWORD))

            print ("code:"+str(response.status_code))
            print ("headers:"+ str(response.headers))
            print ("content:"+ str(response.text))
		
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

    class Meta:
        model = phase_models.Phase
        exclude = ('module', 'type')

        widgets = {
            'end_date': widgets.DateTimeInput(),
            'start_date': widgets.DateTimeInput(),
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


class ProjectCreateForm(multiform.MultiModelForm):

    def __init__(self, blueprint, organisation, creator, *args, **kwargs):
        kwargs['phases__queryset'] = phase_models.Phase.objects.none()
        kwargs['phases__initial'] = [
            {'phase_content': t} for t in blueprint.content
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
        for phase, phase_content in zip(phases, self.blueprint.content):
            phase.module = module
            phase.type = phase_content.identifier
            if commit:
                phase.save()

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
        widgets = {
            'image': widgets.ImageInputWidget(),
            'logo': widgets.ImageInputWidget(),
        }
        labels = {
            'image': _('Header Image'),
        }
        help_texts = {
            'image': _("Your image should be at least 1300px wide and "
                       "600px high. Supported formats are %s."
                       % ", ".join(settings.ALLOWED_UPLOAD_IMAGES)),
            'logo': _("Your logo should be at least 200px wide "
                      "and square. Supported formats are %s."
                      % ", ".join(settings.ALLOWED_UPLOAD_IMAGES))
        }

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
