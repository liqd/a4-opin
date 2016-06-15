from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class Comment(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)

    # Metadata about the comment
    submit_date = models.DateTimeField(editable=False, db_index=True)
    edit_date = models.DateTimeField(editable=False, db_index=True)
    is_removed = models.BooleanField(default=False)
    is_censored = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.submit_date = timezone.now()
        self.edit_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.date_created)
