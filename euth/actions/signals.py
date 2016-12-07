from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from euth.actions import emails
from euth.modules.models import Item
from euth.projects.models import Project

from . import verbs
from .models import Action


def notify_creator(instance):
    if hasattr(instance.target, 'creator'):
        creator = instance.target.creator
        if creator.get_notifications and not creator == instance.actor:
            emails.notify_users_on_create_action(instance, [creator.email])


def notify_moderators(instance):
    if str(instance.target_content_type) == 'project':
        recipients = instance.target.moderators.all().values_list(
            'email', flat=True)
        emails.notify_users_on_create_action(instance, recipients)


def add_action(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    verb = verbs.CREATE if created else verbs.UPDATE
    actor = instance.creator

    action = Action(
        actor=actor,
        verb=verb,
        action_object_content_type=content_type,
        action_object_object_id=instance.pk,
    )

    if str(content_type) == 'Comment':
        project = instance.project if hasattr(
            instance, 'project') and isinstance(
            instance.project, Project) else None

        action.target_content_type = instance.content_type
        action.target_object_id = instance.object_pk
        action.project = project
        action.save()

    elif isinstance(instance, Item):
        project = instance.module.project
        project_contenttype = ContentType.objects.get_for_model(project)

        action.target_content_type = project_contenttype
        action.target_object_id = project.pk
        action.project = project
        action.save()

    else:
        pass


for app, model in settings.ACTIONABLE:
    post_save.connect(add_action, apps.get_model(app, model))


@receiver(post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):

    if instance.verb == verbs.CREATE:
        notify_creator(instance)
        notify_moderators(instance)
    if instance.verb == verbs.COMPLETE:
        emails.notify_followers_on_almost_finished(instance.project)
