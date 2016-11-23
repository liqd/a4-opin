import re
from allauth.account.adapter import DefaultAccountAdapter

from euth.contrib.emails import send_email_with_template
from euth.users import USERNAME_REGEX


class EuthAccountAdapter(DefaultAccountAdapter):
    username_regex = re.compile(USERNAME_REGEX)

    def send_mail(self, template_prefix, email, context):
        return send_email_with_template([email], template_prefix, context)
