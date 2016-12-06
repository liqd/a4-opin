import json

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_init, post_save
from django.dispatch import receiver

from euth.actions.models import Action
from euth.contrib import services

from .models import Idea


@receiver(post_init, sender=Idea)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.image


@receiver(post_save, sender=Idea)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.image:
            services.delete_images([instance._current_image_file])


@receiver(post_delete, sender=Idea)
def delete_images_for_Idea(sender, instance, **kwargs):
    services.delete_images([instance.image])


@receiver(post_delete, sender=Idea)
def delete_comments_for_Idea(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_comments(contenttype, pk)


@receiver(post_delete, sender=Idea)
def delete_ratings_for_Idea(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_ratings(contenttype, pk)


@receiver(post_save, sender=Idea)
def add_action(sender, instance, created, **kwargs):
    project = instance.module.project
    idea_contenttype = ContentType.objects.get_for_model(instance)
    project_contenttype = ContentType.objects.get_for_model(project)

    recipients = project.moderators.all().filter(
        get_notifications=True).values_list('email', flat=True)

    verb = 'created' if created else 'updated'

    Action.objects.create(
        actor=instance.creator,
        target_content_type=project_contenttype,
        target_object_id=project.pk,
        action_object_content_type=idea_contenttype,
        action_object_object_id=instance.pk,
        project=project,
        verb=verb,
        recipients=json.dumps(list(recipients))
    )
