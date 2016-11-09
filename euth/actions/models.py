from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from euth.projects.models import Project


class Action(models.Model):

    # actor
    actor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    # target
    target_content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                            related_name='target')
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    target = GenericForeignKey(
        ct_field='target_content_type', fk_field='target_object_id')

    # action object
    action_object_content_type = models.ForeignKey(
        ContentType,
        blank=True, null=True,
        related_name='action_object')
    action_object_object_id = models.CharField(
        max_length=255, blank=True, null=True)
    action_object = GenericForeignKey(
        ct_field='action_object_content_type',
        fk_field='action_object_object_id')

    # project
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True, db_index=True)
    verb = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
