from django.contrib import auth
from django.utils import translation

from euth.contrib import emails


def notify_users_on_create_action(action, users):
    context = {
        'action': action,
    }

    emails.send_email_with_template(users, 'notify_creator', context)


def notify_followers_on_almost_finished(project):
    translation.activate('en')
    User = auth.get_user_model()
    recipients = User.objects.filter(
        follow__project=project,
        follow__enabled=True,
        get_notifications=True
    )

    context = {
        'project': project,
        'url': project.get_absolute_url()
    }

    emails.send_email_with_template(recipients, 'notify_followers', context)
