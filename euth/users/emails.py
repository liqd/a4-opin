from django.contrib.sites import shortcuts
from django.core.urlresolvers import reverse
from django.template import Context

from euth.contrib import emails


def send_registration(request, registration):
    activation_path = reverse('activate', args=[str(registration.token)])
    context = Context({'registration': registration,
                       'site': shortcuts.get_current_site(request),
                       'activation_url': request.build_absolute_uri(
                           activation_path),
                       })

    emails.send_email_with_template([registration.email], 'register', context)


def send_reset(request, reset):
    reset_path = reverse('reset_password', args=[str(reset.token)])
    context = Context({'reset': reset,
                       'site': shortcuts.get_current_site(request),
                       'reset_url': request.build_absolute_uri(reset_path),
                       })

    emails.send_email_with_template([reset.user.email], 'reset', context)
