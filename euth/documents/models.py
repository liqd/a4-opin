from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from contrib.transforms import html_transforms
from euth.comments import models as comment_models
from euth.contrib import base_models
from euth.modules import models as module_models


class Document(module_models.Item):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "{}_document_{}".format(str(self.module), self.pk)

    def clean(self, *args, **kwargs):
        try:
            Document.objects.get(module=self.module)
            raise ValidationError(_('Document for that module already exists'))
        except ObjectDoesNotExist:
            super().clean(*args, **kwargs)

    @cached_property
    def paragraphs_sorted(self):
        return self.paragraph_set.all().order_by('weight')


class Paragraph(base_models.TimeStampedModel):
    name = models.CharField(max_length=120, blank=True)
    text = RichTextField()
    weight = models.PositiveIntegerField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_paragraph_{}".format(str(self.document), self.weight)

    def save(self, *args, **kwargs):
        self.text = html_transforms.clean_html_field(
            self.text)
        super().save(*args, **kwargs)

    @cached_property
    def comments(self):
        contenttype = ContentType.objects.get_for_model(self)
        pk = self.id
        comments = comment_models.Comment.objects.all().filter(
            content_type=contenttype, object_pk=pk)
        return comments
