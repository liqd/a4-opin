from django.conf import settings
from django.template.loader import select_template
from django.template import Context
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils.translation import get_language

def _send_email_with_template(receiver, template, context):
    languages = [ get_language(), 'en' ]
    subject = select_template([ 'emails/{}.{}.subject'.format(template, lang) for lang in languages ])
    plaintext = select_template([ 'emails/{}.{}.txt'.format(template, lang) for lang in languages ])
    html = select_template([ 'emails/{}.{}.html'.format(template, lang) for lang in languages ])

    send_mail(
        subject=subject.render(context).strip(),
        message=plaintext.render(context),
        html_message=html.render(context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[receiver])


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
