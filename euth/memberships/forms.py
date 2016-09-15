from django import forms
from django.core.exceptions import ValidationError

from . import models


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
