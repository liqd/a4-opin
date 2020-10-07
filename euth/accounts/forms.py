import collections
from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _

from euth.contrib import widgets
from euth.users.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', '_avatar', 'description', 'birthdate',
                  'country', 'city', 'timezone', 'gender', 'languages',
                  'twitter_handle', 'facebook_handle', 'instagram_handle',
                  'get_notifications']
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
                'timezone',
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

    def clean_birthdate(self):
        birthday = self.cleaned_data['birthdate']
        if birthday:
            today = date.today()
            if birthday > today:
                raise forms.ValidationError(_('You are not yet born. Please '
                                              'enter a date in the past.'))
        return birthday
