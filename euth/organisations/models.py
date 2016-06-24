from django.conf import settings
from django.db import models
from model_utils import models as model_utils


class OrganisationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Organisation(model_utils.TimeStampedModel):
    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True)
    description_why = models.TextField()
    description_how = models.TextField()
    description = models.TextField()
    initiators = models.ManyToManyField(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='organisations/images', blank=True)
    logo = models.ImageField(upload_to='organisations/logos', blank=True)

    objects = OrganisationManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('organisation-detail', args=[str(self.slug)])
