from django.conf import settings
from django.db import models
from django_countries import fields as countries_fields
from parler.models import (TranslatableManager, TranslatableModel,
                           TranslatedFields)

from adhocracy4.images import validators
from adhocracy4.models import base


class OrganisationManager(TranslatableManager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Organisation(base.TimeStampedModel, TranslatableModel):
    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True)

    translations = TranslatedFields(
        title=models.CharField(max_length=512),
        description_why=models.TextField(),
        description_how=models.TextField(),
        description=models.TextField(),
    )

    initiators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='organisations/images', blank=True,
                              validators=[validators.validate_hero_image])
    logo = models.ImageField(upload_to='organisations/logos', blank=True,
                             validators=[validators.validate_logo])
    twitter_handle = models.CharField(max_length=200, blank=True)
    facebook_handle = models.CharField(max_length=200, blank=True)
    instagram_handle = models.CharField(max_length=200, blank=True)
    webpage = models.URLField(blank=True)
    country = countries_fields.CountryField()
    place = models.CharField(max_length=200)

    objects = OrganisationManager()

    def __str__(self):
        return self.name

    def has_social_share(self):
        return (
            self.twitter_handle or self.facebook_handle
            or self.instagram_handle or self.webpage
        )

    def has_initiator(self, user):
        return user in self.initiators.all()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('organisation-detail', args=[str(self.slug)])
