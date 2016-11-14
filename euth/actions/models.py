from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince as djtimesince
from django.utils.translation import ugettext as _

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
        Project, on_delete=models.CASCADE, blank=True, null=True)

    timestamp = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=True, db_index=True)
    verb = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        ctx = {
            'actor': self.actor,
            'verb': self.verb,
            'action_object': self.action_object,
            'target': self.target,
            'timesince': self.timesince()
        }
        if self.target:
            if self.action_object:
                return _('%(actor)s %(verb)s '
                         '%(action_object)s on '
                         '%(target)s %(timesince)s ago') % ctx
            return _('%(actor)s %(verb)s '
                     '%(target)s %(timesince)s ago') % ctx
        if self.action_object:
            return _('%(actor)s %(verb)s '
                     '%(action_object)s %(timesince)s ago') % ctx
        return _('%(actor)s %(verb)s %(timesince)s ago') % ctx

    def timesince(self, now=None):
        res = djtimesince(self.timestamp, now).encode('utf8')
        res = res.replace(b'\xc2\xa0', b' ').decode('utf8')
        return res
