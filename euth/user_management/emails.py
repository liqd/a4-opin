import os
from email.encoders import encode_base64
from email.mime.image import MIMEImage

from django.conf import settings
from django.template.loader import select_template
from django.template import Context
from django.core.mail.message import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.utils.translation import get_language

def _send_email_with_template(receiver, template, context):
    languages = [ get_language(), 'en' ]
    subject = select_template([ 'emails/{}.{}.subject'.format(template, lang) for lang in languages ])
    plaintext = select_template([ 'emails/{}.{}.txt'.format(template, lang) for lang in languages ])
    html = select_template([ 'emails/{}.{}.html'.format(template, lang) for lang in languages ])

    mail = EmailMultiAlternatives(
        subject=subject.render(context).strip(),
        body=plaintext.render(context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[ receiver ],
    )
    mail.mixed_subtype = 'related'
    with open(os.path.join(settings.STATIC_ROOT, 'images', 'logo.png'), 'rb') as f:
        opin_logo = MIMEImage(f.read())
        opin_logo.add_header('Content-ID', '<{}>'.format('opin_logo'))
        mail.attach(opin_logo)
    mail.attach_alternative(html.render(context), 'text/html')
    mail.send()

def send_registration(request, registration):
    context = Context({'registration': registration,
                       'sitename': request.get_host(),
                       'activation_url': request.build_absolute_uri(
                           reverse('activate', args=[str(registration.token)])),
                       })

    _send_email_with_template(registration.email, "register", context)


def send_reset(request, reset):
    context = Context({'reset': reset,
                       'sitename': request.get_host(),
                       'reset_url': request.build_absolute_uri(
                           reverse('reset_password', args=[str(reset.token)])),
                       })

    _send_email_with_template(reset.user.email, "reset", context)
