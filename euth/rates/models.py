from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from euth.contrib.base_models import TimeStampedModel


class Rate(TimeStampedModel):

    POSITIVE = 1
    NEGATIVE = -1

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
        if number > self.POSITIVE:
            return self.POSITIVE
        elif number < self.NEGATIVE:
            return self.NEGATIVE
        else:
            return number

    def get_meta_info(self, user):

        rates = Rate.objects.filter(
            content_type=self.content_type, object_pk=self.object_pk)
        positive_rates_on_same_object = rates.filter(
            value=self.POSITIVE).count()
        negative_rates_on_same_object = rates.filter(
            value=self.NEGATIVE).count()

        try:
            user_rate_on_same_object = rates.get(user=user)
            user_rate_on_same_object_value = user_rate_on_same_object.value
            user_rate_on_same_object_id = user_rate_on_same_object.pk
        except ObjectDoesNotExist:
            user_rate_on_same_object_value = None
            user_rate_on_same_object_id = None

        result = {
            'positive_rates_on_same_object': positive_rates_on_same_object,
            'negative_rates_on_same_object': negative_rates_on_same_object,
            'user_rate_on_same_object_value': user_rate_on_same_object_value,
            'user_rate_on_same_object_id': user_rate_on_same_object_id
        }

        return result
