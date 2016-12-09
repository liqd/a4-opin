from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from adhocracy4.models import base
from contrib.transforms import html_transforms
from euth.comments import models as comment_models
from euth.modules import models as module_models


class Document(module_models.Item):
    name = models.CharField(max_length=120)
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='document',
                               object_id_field='object_pk')

    def __str__(self):
        return "{}_document_{}".format(str(self.module), self.pk)

    def clean(self, *args, **kwargs):
        if not self.pk:
            try:
                Document.objects.get(module=self.module)
                raise ValidationError(
                    _('Document for that module already exists'))
            except ObjectDoesNotExist:
                super().clean(*args, **kwargs)
        super().clean(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project-detail', args=[str(self.project.slug)])


class Paragraph(base.TimeStampedModel):
    name = models.CharField(max_length=120, blank=True)
    text = RichTextField()
    weight = models.PositiveIntegerField()
    document = models.ForeignKey(Document,
                                 on_delete=models.CASCADE,
                                 related_name='paragraphs')
    comments = GenericRelation(comment_models.Comment,
                               related_query_name='paragraph',
                               object_id_field='object_pk')

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return "{}_paragraph_{}".format(str(self.document), self.weight)

    def save(self, *args, **kwargs):
        self.text = html_transforms.clean_html_field(
            self.text, 'image-editor')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('paragraph-detail', args=[str(self.pk)])

    @cached_property
    def creator(self):
        return self.document.creator

    @cached_property
    def project(self):
        return self.document.project
