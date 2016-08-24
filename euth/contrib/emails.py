from email.mime.image import MIMEImage

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import select_template
from django.utils.translation import get_language


def send_email_with_template(receivers, template, context):
    languages = [get_language(), 'en']
    subject = select_template(['emails/{}.{}.subject'.format(template, lang)
                               for lang in languages])
    plaintext = select_template(['emails/{}.{}.txt'.format(template, lang)
                                 for lang in languages])
    html = select_template(['emails/{}.{}.html'.format(template, lang)
                            for lang in languages])

    mail = EmailMultiAlternatives(
        subject=subject.render(context).strip(),
        body=plaintext.render(context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=receivers,
    )
    mail.mixed_subtype = 'related'
    filename = finders.find('images/logo.png')
    f = open(filename, 'rb')
    opin_logo = MIMEImage(f.read())
    opin_logo.add_header('Content-ID', '<{}>'.format('opin_logo'))
    mail.attach(opin_logo)
    mail.attach_alternative(html.render(context), 'text/html')
    mail.send()
