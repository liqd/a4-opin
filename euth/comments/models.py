from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from euth.contrib.base_models import TimeStampedModel


class Comment(TimeStampedModel):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
    is_removed = models.BooleanField(default=False)
    is_censored = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return str(self.created)

    @property
    def process(self):
        co = self.content_object
        if isinstance(co, self.__class__):
            co = co.content_object
        return co.process

    def save(self, *args, **kwargs):
        """
        Change the text of the comment if
        the comment was marked removed or censored
        """

        if self.is_removed:
            self.comment = 'deleted by creator'
        if self.is_censored:
            self.comment = 'deleted by moderator'
        return super(Comment, self).save(*args, **kwargs)
