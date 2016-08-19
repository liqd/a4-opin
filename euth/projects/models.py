from django.conf import settings
from django.db import models
from django.utils import functional

from euth.contrib import base_models, validators
from euth.organisations import models as org_models


class ProjectManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Project(base_models.TimeStampedModel):
    slug = models.SlugField(max_length=512, unique=True)
    name = models.CharField(max_length=512)
    organisation = models.ForeignKey(
        org_models.Organisation, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    information = models.TextField()
    is_public = models.BooleanField(default=True)
    is_draft = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='projects/backgrounds',
        blank=True,
        validators=[validators.validate_hero_image])
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='project_participant',
        blank=True,
    )
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='project_moderator'
    )

    objects = ProjectManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project-detail', args=[str(self.slug)])

    @functional.cached_property
    def other_projects(self):
        other_projects = self.organisation.project_set.all().exclude(
            slug=self.slug)
        return other_projects

    @functional.cached_property
    def is_private(self):
        return not self.is_public

    @functional.cached_property
    def active_phase(self):
        module = self.module_set.first()
        return module.phase_set.order_by('type').first()
