from django.db.models.signals import post_save
from django.dispatch import receiver

from euth.actions import emails

from . import verbs
from .models import Action


@receiver(post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):

    if instance.verb == verbs.CREATE and hasattr(instance.target, 'creator'):
        creator = instance.target.creator
        if creator.get_notifications and not creator == instance.actor:
            emails.notify_creator_on_create_action(instance)
for app, model in settings.ACTIONABLE:
    post_save.connect(add_action, apps.get_model(app, model))
    if instance.verb == verbs.COMPLETE:
        emails.notify_followers_on_almost_finished(instance.project)
