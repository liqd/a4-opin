import email.utils
import re

from betterforms.multiform import MultiModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from euth.contrib import widgets
from euth.memberships import models as member_models
from euth.modules import models as module_models
from euth.phases import models as phase_models
from euth.projects import models as project_models
from euth.users import models as user_models


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


class PhaseCreateForm(forms.ModelForm):

    class Meta:
        model = phase_models.Phase
        exclude = ('module', )
        widgets = {'type': forms.HiddenInput()}


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = project_models.Project
        fields = ['image', 'name', 'description', 'information', 'is_public',
                  'result']
        widgets = {
            'image': widgets.ImageInputWidget()
        }


class ProjectCreateMultiForm(MultiModelForm):

    def __init__(self, *args, **kwargs):
        self.extras = kwargs['phase_extras']
        del kwargs['phase_extras']
        self.organisation = kwargs['organisation']
        del kwargs['organisation']
        super().__init__(*args, **kwargs)

    @property
    def form_classes(self):
        return {
            'project': ProjectCreateForm,
            'phase': modelformset_factory(phase_models.Phase,
                                          PhaseCreateForm,
                                          extra=self.extras)
        }

    def get_form_args_kwargs(self, key, args, kwargs):
        fargs, fkwargs = super().get_form_args_kwargs(key, args, kwargs)
        if key == 'phase':
            queryset = {'queryset': phase_models.Phase.objects.none()}
            queryset.update(fkwargs)
            return (args, queryset)

        return (args, kwargs)

    def is_valid(self):
        forms_valid = all(form.is_valid() for form in self.forms.values())
        try:
            self.clean()
        except ValidationError as e:
            self.add_crossform_error(e)
        # else:
        #    if cleaned_data is not None:
        #        for key, data in cleaned_data.items():
        #            self.forms[key].cleaned_data = data
        return forms_valid and not self.crossform_errors

    def save(self, commit=True):
        objects = super().save(commit=False)

        if commit:
            project = objects['project']
            project.organisation = self.organisation
            project.is_draft = False
            project.save()
            module = module_models.Module()
            module.name = project.slug + '_module'
            module.weight = 1
            module.project = project
            module.save()
            phases = objects['phase']
            for phase in phases:
                phase.module = module
                phase.save()

        return objects
