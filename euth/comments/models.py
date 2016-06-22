from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone


class Comment(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
    submit_date = models.DateTimeField(editable=False, db_index=True)
    edit_date = models.DateTimeField(editable=False, db_index=True)
    is_removed = models.BooleanField(default=False)
    is_censored = models.BooleanField(default=False)

    def __str__(self):
        return str(self.submit_date)

    def save(self, *args, **kwargs):
        """
        Set create and update time and change the text of the
        comment if the comment was marked removed or censored
        """
        if not self.id:
            self.submit_date = timezone.now()
        self.edit_date = timezone.now()
        if self.is_removed:
            self.comment = 'deleted by creator'
        if self.is_censored:
            self.comment = 'deleted by moderator'
        return super(Comment, self).save(*args, **kwargs)
