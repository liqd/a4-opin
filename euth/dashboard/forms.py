import email.utils
import re

import multiform
from django import forms
from django.core.exceptions import ValidationError

from euth.contrib import widgets
from euth.memberships import forms as member_forms
from euth.memberships import models as member_models
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


class ProjectUserForm(multiform.MultiModelForm):
    base_forms = [
        ('requests', forms.modelformset_factory(
            member_models.Request,
            member_forms.RequestModerationForm,
            extra=0)),
        ('invites', forms.modelformset_factory(
            member_models.Invite,
            member_forms.InviteModerationForm,
            extra=0)),
    ]

    def _init_wrapped_forms(self, sig_kwargs, extra_kwargs):
        """
        Filter our arguments that don't make sense for formsets as base_forms.
        Should be moved to multiforms itself.
        """
        new_sig_kwargs = dict(sig_kwargs)
        del new_sig_kwargs['instance']
        del new_sig_kwargs['empty_permitted']
        del new_sig_kwargs['label_suffix']
        return super()._init_wrapped_forms(new_sig_kwargs, extra_kwargs)

    def _combine(self, *args, **kwargs):
        """
        Filter out list of falsy values which occour when using formsets.
        Should be moved to multiforms itself.
        """
        values = super()._combine(*args, **kwargs)
        if 'filter' in kwargs and kwargs['filter']:
            values = [
                value for value in values
                if not hasattr(value, '__iter__') or not any(value)
            ]
        return values

    def full_clean(self):
        """
        Modified full clean that does collect cleaned data from formsets.
        Should be moved to multiforms itself.
        """
        self._errors = self._combine('errors', filter=True)

        if not self._errors:
            self.cleaned_data = {}
            for name, formset in self.forms.items():
                self.cleaned_data[name] = [f.cleaned_data for f in formset]

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
