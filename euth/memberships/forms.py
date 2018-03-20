import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from euth.users.models import User

from . import models


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
        model = models.Request
        fields = ['action']


class InviteForm(forms.ModelForm):
    accept = forms.CharField(required=False)
    reject = forms.CharField(required=False)

    class Meta:
        model = models.Invite
        fields = ['accept', 'reject']

    def clean(self):
        data = self.data
        if 'accept' not in data and 'reject' not in data:
            raise ValidationError('Reject or accept')
        return data

    def is_accepted(self):
        data = self.data
        return 'accept' in data and 'reject' not in data


class InviteModerationForm(forms.ModelForm):
    delete = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = models.Invite
        fields = ['delete']


class ParticipantsModerationForm(forms.ModelForm):
    delete = forms.BooleanField(initial=False, required=False)

    class Meta:
        model = User
        fields = ['delete']


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
        existing = models.Invite.objects.filter(**query) \
            .values_list('email', flat=True)
        if existing:
            for address in existing:
                raise ValidationError(
                    '{} already invited'.format(address)
                )
        return emails
