from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import functional
from adhocracy4 import transforms

from adhocracy4.comments import models as comment_models
from adhocracy4.models import base
from adhocracy4.phases import models as phase_models

from . import validators


class Offlinephase(base.TimeStampedModel):
    text = RichTextField(blank=True, config_name='image-editor')
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
            self.text, 'image-editor')
        super().save(*args, **kwargs)

    @functional.cached_property
    def project(self):
        return self.phase.module.project

    @functional.cached_property
    def module(self):
        return self.phase.module

    @functional.cached_property
    def organisation(self):
        return self.project.organisation


def document_path(instance, filename):
    return 'documents/offlinephase_{}/{}'.format(
        instance.offlinephase.pk, filename)


class FileUpload(base.TimeStampedModel):
    title = models.CharField(max_length=256)
    document = models.FileField(
        upload_to=document_path,
        validators=[validators.validate_file_type_and_size])
    offlinephase = models.ForeignKey(Offlinephase)
