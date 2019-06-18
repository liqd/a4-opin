import re
from urllib.parse import quote

from allauth.account.adapter import DefaultAccountAdapter
from django.utils.http import is_safe_url

from adhocracy4.emails import Email
from adhocracy4.emails.mixins import SyncEmailMixin
from euth.users import USERNAME_REGEX


class EuthAccountEmail(SyncEmailMixin, Email):
    def get_receivers(self):
        return [self.object]

    @property
    def template_name(self):
        return self.kwargs['template_name']


class EuthAccountAdapter(DefaultAccountAdapter):
    username_regex = re.compile(USERNAME_REGEX)

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = super().get_email_confirmation_url(request, emailconfirmation)
        if 'next' in request.POST and is_safe_url(request.POST['next'],
                                                  allowed_hosts=None):
            return '{}?next={}'.format(url, quote(request.POST['next']))
        else:
            return url

    def send_mail(self, template_prefix, email, context):
        return EuthAccountEmail.send(
            email,
            template_name=template_prefix,
            **context
        )

    def get_email_confirmation_redirect_url(self, request):
        if 'next' in request.GET and is_safe_url(request.GET['next'],
                                                 allowed_hosts=None):
            return request.GET['next']
        else:
            return super().get_email_confirmation_redirect_url(request)
