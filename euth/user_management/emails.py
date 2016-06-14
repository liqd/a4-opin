from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.core.urlresolvers import reverse


def send_registration(request, registration):
    context = Context({'registration': registration,
                       'sitename': request.get_host(),
                       'activation_url': request.build_absolute_uri(
                           reverse('activate', args=[str(registration.token)])),
                       })
    plaintext = get_template('emails/register.txt')
    subject = get_template('emails/register.subject')
    html = get_template('emails/register.html')

    send_mail(
        subject=subject.render(context).strip(),
        message=plaintext.render(context),
        html_message=plaintext.render(context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[registration.email])
