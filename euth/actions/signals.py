from django.db.models.signals import post_save
from django.dispatch import receiver

from euth.actions import emails

from .models import Action


@receiver(post_save, sender=Action)
def send_notification(sender, instance, created, **kwargs):

    if instance.verb == 'created':
        emails.notify_creator_on_create_action(instance)
    if instance.verb == 'project almost finished':
        emails.notify_followers_on_almost_finished(instance.project)
