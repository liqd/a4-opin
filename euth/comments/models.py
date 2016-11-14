from django.conf import settings
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from euth.contrib.base_models import UserGeneratedContentModel
from euth.contrib.generics import models_to_limit
from euth.ratings import models as rating_models


class Comment(UserGeneratedContentModel):

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=models_to_limit(settings.COMMENTABLES)
    )
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    comment = models.TextField(max_length=1024)
    is_removed = models.BooleanField(default=False)
    is_censored = models.BooleanField(default=False)
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='comment',
                              object_id_field='object_pk')
    child_comments = GenericRelation('self',
                                     related_query_name='parent_comment',
                                     object_id_field='object_pk')

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('created',)

    def __str__(self):
        if len(self.comment) > 50:
            return "comment: {} ...".format(self.comment[:50])
        else:
            return "comment: {}".format(self.comment)

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

    def get_absolute_url(self):
        if hasattr(self.content_object, 'get_absolute_url'):
            return self.content_object.get_absolute_url()
        elif hasattr(self.project, 'get_absolute_url'):
            return self.project.get_absolute_url()
        else:
            return None

    @property
    def notification_content(self):
        return self.comment

    @property
    def project(self):
        co = self.content_object
        if isinstance(co, self.__class__):
            co = co.content_object
        return co.project
