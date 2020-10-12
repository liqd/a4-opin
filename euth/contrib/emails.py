from email.mime.image import MIMEImage

from django.contrib.staticfiles import finders

from adhocracy4.emails.mixins import Email
from adhocracy4.emails.mixins import SyncEmailMixin


class OpinEmail(SyncEmailMixin, Email):
    def get_attachments(self):
        attachments = super().get_attachments()
        filename = finders.find('images/logo.png')
        f = open(filename, 'rb')
        opin_logo = MIMEImage(f.read())
        opin_logo.add_header('Content-ID', '<{}>'.format('opin_logo'))
        return attachments + [opin_logo]
