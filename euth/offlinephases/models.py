from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from adhocracy4 import transforms

from adhocracy4.comments import models as comment_models
from adhocracy4.models import base
from adhocracy4.phases import models as phase_models


class Offlinephase(base.TimeStampedModel):
    text = RichTextField()
    phase = models.OneToOneField(
        phase_models.Phase,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='offlinephase'
    )
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='offlinephase',
                               object_id_field='object_pk')

    def __str__(self):
        return "{}_offlinephase_{}".format(str(self.phase), self.pk)

    def save(self, *args, **kwargs):
        self.text = transforms.clean_html_field(
            self.text)
        super().save(*args, **kwargs)
