from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from euth.contrib.base_models import TimeStampedModel


class Rate(TimeStampedModel):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        unique_together = (('content_type', 'object_pk', 'user'))

    def __str__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        self.value = self._get_value(self.value)
        return super().save(*args, **kwargs)

    def _get_value(self, number):
        if number > 1:
            return 1
        elif number < -1:
            return -1
        else:
            return number
