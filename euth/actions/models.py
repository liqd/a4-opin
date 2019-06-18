from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from adhocracy4.projects.models import Project

from . import verbs


class Action(models.Model):

    # actor, if actor is None the action was create by the system
    actor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)

    # target eg. idea
    target_content_type = models.ForeignKey(ContentType,
                                            blank=True,
                                            null=True,
                                            on_delete=models.CASCADE,
                                            related_name='target')
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    target = GenericForeignKey(
        ct_field='target_content_type', fk_field='target_object_id')

    # action object eg. comment
    action_object_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='action_object')
    action_object_object_id = models.CharField(
        max_length=255, blank=True, null=True)
    action_object = GenericForeignKey(
        ct_field='action_object_content_type',
        fk_field='action_object_object_id')

    # project
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)

    timestamp = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True, db_index=True)
    verb = models.CharField(max_length=255, db_index=True, choices=verbs.all())
    description = models.TextField(blank=True, null=True)

    def __str__(self):

        ctx = {
            'actor': self.actor.username if self.actor else 'system',
            'verb': self.verb,
            'action_object': self.action_object,
            'target': self.target
        }

        if self.target:
            if self.action_object:
                return '{actor} {verb} {action_object} on {target}'.format(
                    **ctx)
            return '{actor} {verb} {target}'.format(**ctx)
        if self.action_object:
            return '{actor} {verb} {action_object}'.format(**ctx)
        return '{actor} {verb}'.format(**ctx)
