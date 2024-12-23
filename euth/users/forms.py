from zoneinfo import available_timezones

from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

from euth.captcha.fields import CaptcheckCaptchaField

User = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    """SignUpForm used by django-allouth to create new users."""

    terms_of_use = forms.BooleanField()
    timezone = forms.CharField(widget=forms.HiddenInput(), required=False)
    captcha = CaptcheckCaptchaField(label='I am not a robot')

    def clean_timezone(self):
        timezone = self.cleaned_data['timezone']
        if timezone not in available_timezones():
            timezone = ""
        return timezone

    def signup(self, request, user):
        user.signup(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['timezone'],
        )

    class Meta:
        model = User
        fields = ('email', 'username', 'terms_of_use', 'timezone')
