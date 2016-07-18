from django.conf import settings
from django.db import models
from model_utils import models as model_utils
from parler.models import (TranslatableManager, TranslatableModel,
                           TranslatedFields)

from euth.contrib import validators


class OrganisationManager(TranslatableManager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Organisation(model_utils.TimeStampedModel, TranslatableModel):
    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=512),
        description_why = models.TextField(),
        description_how = models.TextField(),
        description = models.TextField(),
    )

    initiators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='organisations/images', blank=True,
                              validators=[validators.validate_hero_image])
    logo = models.ImageField(upload_to='organisations/logos', blank=True,
                             validators=[validators.validate_logo])

    objects = OrganisationManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('organisation-detail', args=[str(self.slug)])
