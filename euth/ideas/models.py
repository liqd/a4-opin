from autoslug import AutoSlugField
from django.db import models
from django.utils.functional import cached_property

from ckeditor.fields import RichTextField
from contrib.transforms import html_transforms
from euth.contrib import validators
from euth.modules import models as module_models


class Idea(module_models.Item):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=512)
    description = RichTextField()
    image = models.ImageField(upload_to='ideas/images', blank=True,
                              validators=[validators.validate_hero_image])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('idea-detail', args=[str(self.slug)])

    def clean(self):
        super().clean()
        self.description = html_transforms.clean_html_field(
            self.description)

    @cached_property
    def project(self):
        return self.module.project
