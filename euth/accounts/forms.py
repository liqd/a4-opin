import collections

from django import forms
from django.utils.translation import gettext_lazy as _

from euth.users.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']

    @property
    def formsections(self):
        formsections = collections.OrderedDict([
            (_('Basic Info'), [
                'username',
            ]),
        ])

        return formsections

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username__iexact=username)
            if user != self.instance:
                raise forms.ValidationError(
                    User._meta.get_field('username').error_messages['unique'])
        except User.DoesNotExist:
            pass

        return username
