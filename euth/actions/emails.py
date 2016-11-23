from django.contrib import auth
from django.utils import translation

from euth.contrib import emails


def notify_creator_on_create_action(action):
    title = action.target.name if hasattr(action.target, 'name') else None
    content = action.action_object.notification_content if hasattr(
        action.action_object, 'notification_content') else None
    url = action.target.get_absolute_url() if hasattr(
        action.target, 'get_absolute_url') else None

    context = {
        'object_verbose_name': action.action_object._meta.verbose_name,
        'target_object_verbose_name': action.target._meta.verbose_name,
        'target_object_title': title,
        'notification_content': content,
        'url': url,
    }

    emails.send_email_with_template(
        [action.target.creator.email], 'notify_creator', context)


def notify_followers_on_almost_finished(project):
    translation.activate('en')
    User = auth.get_user_model()
    recipients = User.objects.filter(
        follow__project=project).filter(
        follow__enabled=True).filter(
        get_notifications=True
    ).values_list('email', flat=True)

    context = {
        'project': project,
        'url': project.get_absolute_url()
    }

    emails.send_email_with_template(
        recipients, 'notify_followers', context)
