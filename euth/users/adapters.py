from allauth.account.adapter import DefaultAccountAdapter

from euth.contrib.emails import send_email_with_template


class EuthAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        return send_email_with_template([email], template_prefix, context)
