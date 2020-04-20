from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse

from adhocracy4.modules import models as module_models


class Topic(module_models.Item):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120)
    description = RichTextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.slug)])
