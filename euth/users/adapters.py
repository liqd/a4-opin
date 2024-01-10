import re
from urllib.parse import quote

from allauth.account.adapter import DefaultAccountAdapter
from django.utils.http import url_has_allowed_host_and_scheme

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

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse

        (Comment reproduced from the overridden method.)
        """
        return False

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = super().get_email_confirmation_url(request, emailconfirmation)
        if 'next' in request.POST \
            and url_has_allowed_host_and_scheme(request.POST['next'],
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
        if 'next' in request.GET \
            and url_has_allowed_host_and_scheme(request.GET['next'],
                                                allowed_hosts=None):
            return request.GET['next']
        else:
            return super().get_email_confirmation_redirect_url(request)
