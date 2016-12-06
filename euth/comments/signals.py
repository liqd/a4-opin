from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from euth.actions import verbs
from euth.actions.models import Action
from euth.contrib import services

from euth.projects.models import Project

from .models import Comment


@receiver(post_save, sender=Comment)
def add_action(sender, instance, created, **kwargs):
    comment_contenttype = ContentType.objects.get_for_model(instance)
    project = instance.project if hasattr(instance, 'project') and isinstance(
        instance.project, Project) else None

    if created:
        Action.objects.create(
            actor=instance.creator,
            target_content_type=instance.content_type,
            target_object_id=instance.object_pk,
            action_object_content_type=comment_contenttype,
            action_object_object_id=instance.pk,
            project=project,
            verb=verbs.CREATE
        )
    else:
        Action.objects.create(
            actor=instance.creator,
            target_content_type=instance.content_type,
            target_object_id=instance.object_pk,
            action_object_content_type=comment_contenttype,
            action_object_object_id=instance.pk,
            project=project,
            verb=verbs.UPDATE
        )


@receiver(post_delete, sender=Comment)
def delete_comments_for_Comment(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_comments(contenttype, pk)


@receiver(post_delete, sender=Comment)
def delete_ratings_for_Comment(sender, instance, **kwargs):
    contenttype = ContentType.objects.get_for_model(instance)
    pk = instance.pk
    services.delete_ratings(contenttype, pk)
