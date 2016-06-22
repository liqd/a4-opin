from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import make_password

from .models import Registration, Reset

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise ValidationError(_('password mismatch'))
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        required=True)
    password_repeat = forms.CharField(
        widget=forms.PasswordInput, required=True)

    def clean_password_repeat(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_repeat')
        if password1 != password2:
            raise ValidationError(_('passwords dont match'))
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(
            username=username).first() is not None
        register_exits = Registration.objects.filter(
            username=username).first() is not None

        if user_exists or register_exits:
            raise ValidationError(_('username taken'))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_exists = User.objects.filter(email=email).first()
        register_exists = Registration.objects.filter(email=email).first()
        if user_exists or register_exists:
            raise ValidationError(_('email in use'))
        return email

    def register(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        registration = Registration(username=username,
                                    email=email,
                                    password=make_password(password))
        return registration


class ActivateForm(forms.Form):
    token = forms.UUIDField(widget=forms.HiddenInput(), required=True)

    def clean_token(self):
        token = self.cleaned_data.get('token')
        registration = Registration.objects.filter(token=token).first()
        if not registration:
            raise ValidationError(_('invalid token'))
        else:
            self.cleaned_data['registration'] = registration
        return token

    def activate(self, request):
        registration = self.cleaned_data.get('registration')
        user = User(username=registration.username,
                    email=registration.email,
                    password=registration.password)
        return user, registration

class RequestResetForm(forms.Form):
    username_or_email = forms.CharField(max_length=255)

    def clean_username_or_email(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        user = (User.objects.filter(username=username_or_email).first() or
                User.objects.filter(email=username_or_email).first())
        if not user:
            raise ValidationError(_('unkown user'))
        else:
            self.cleaned_data['user'] = user
            return username_or_email

    def request_reset(self, request):
        user = self.cleaned_data.get('user')
        return Reset(user=user)


class ResetForm(forms.Form):
    token = forms.UUIDField(widget=forms.HiddenInput(), required=True)
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        required=True)
    password_repeat = forms.CharField(
        widget=forms.PasswordInput,
        required=True)

    def clean_token(self):
        token = self.cleaned_data.get('token')
        reset = Reset.objects.filter(token=token).first()
        if not reset:
            ValidationError(_('invalid token'))
        else:
            self.cleaned_data['reset'] = reset
        return token

    def clean_password_repeat(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_repeat')
        if password1 != password2:
            raise ValidationError(_('passwords dont match'))
        return password2

    def reset_password(self, request):
        reset = self.cleaned_data.get('reset')
        password = self.cleaned_data.get('password')
        user = reset.user
        user.password = make_password(password)
        return user, reset
