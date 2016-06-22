from django.conf import settings
from django.template.loader import select_template
from django.template import Context
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils.translation import get_language


def send_registration(request, registration):
    context = Context({'registration': registration,
                       'sitename': request.get_host(),
                       'activation_url': request.build_absolute_uri(
                           reverse('activate', args=[str(registration.token)])),
                       })
    languages = [ get_language(), 'en' ]
    plaintext = select_template([ 'emails/register.{}.txt'.format(lang) for lang in languages ])
    subject = select_template([ 'emails/register.{}.subject'.format(lang) for lang in languages ])
    html = select_template([ 'emails/register.{}.html'.format(lang) for lang in languages ])

    send_mail(
        subject=subject.render(context).strip(),
        message=plaintext.render(context),
        html_message=html.render(context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[registration.email])
