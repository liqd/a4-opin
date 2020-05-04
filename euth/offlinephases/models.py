from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import functional
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import transforms
from adhocracy4.comments import models as comment_models
from adhocracy4.models import base
from adhocracy4.phases import models as phase_models
from adhocracy4.projects import models as project_models
from euth.contrib import validators


class Offlinephase(base.TimeStampedModel):
    text = RichTextUploadingField(blank=True, config_name='image-editor',)
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


class OfflineEvent(base.TimeStampedModel):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120, verbose_name=_('Title'))
    date = models.DateTimeField(verbose_name=_('Date'))
    description = RichTextUploadingField(
        config_name='image-editor', verbose_name=_('Description'))
    project = models.ForeignKey(
        project_models.Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = transforms.clean_html_field(
            self.description, 'image-editor')
        super().save(*args, **kwargs)


def document_path(instance, filename):
    return 'documents/offlineevent_{}/{}'.format(
        instance.offlineevent.pk, filename)


class FileUpload(base.TimeStampedModel):
    title = models.CharField(max_length=256)
    document = models.FileField(
        upload_to=document_path,
        validators=[validators.validate_file_type_and_size])
    offlinephase = models.ForeignKey(
        Offlinephase,
        on_delete=models.CASCADE
    )


class OfflineEventFileUpload(base.TimeStampedModel):
    title = models.CharField(max_length=256)
    document = models.FileField(
        upload_to='offlineevents/documents',
        validators=[validators.validate_file_type_and_size])
    offlineevent = models.ForeignKey(
        OfflineEvent,
        on_delete=models.CASCADE
    )
