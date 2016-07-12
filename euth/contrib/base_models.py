from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):

    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk is None:
            self.modified = timezone.now()
        super(TimeStampedModel, self).save(*args, **kwargs)
