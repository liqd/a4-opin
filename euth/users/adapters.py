import re

from allauth.account.adapter import DefaultAccountAdapter

from euth.contrib.emails import send_email_with_template
from euth.users import USERNAME_REGEX


class EuthAccountAdapter(DefaultAccountAdapter):
    username_regex = re.compile(USERNAME_REGEX)

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = super().get_email_confirmation_url(request, emailconfirmation)
        if 'next' in request.POST:
            return '{}?next={}'.format(url, request.POST['next'])
        else:
            return url

    def send_mail(self, template_prefix, email, context):
        return send_email_with_template([email], template_prefix, context)

    def get_email_confirmation_redirect_url(self, request):
        if 'next' in request.GET:
            return request.GET['next']
        else:
            return super().get_email_confirmation_redirect_url(request)
