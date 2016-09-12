from django.conf import settings
from django.db import models
from django.utils import functional, timezone

from contrib.transforms import html_transforms
from euth.contrib import base_models, validators
from euth.organisations import models as org_models


class ProjectManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def featured(self):
        return self.filter(is_draft=False).order_by('-created')[:8]


class Project(base_models.TimeStampedModel):
    slug = models.SlugField(max_length=512, unique=True)
    name = models.CharField(max_length=512)
    organisation = models.ForeignKey(
        org_models.Organisation, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    information = models.TextField()
    result = models.TextField(blank=True)
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

    def save(self, *args, **kwargs):
        self.information = html_transforms.clean_html_field(
            self.information)
        self.result = html_transforms.clean_html_field(
            self.result)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project-detail', args=[str(self.slug)])

    def has_member(self, user):
        """
        Everybody is member of all public projects and private projects can
        be joined as moderator or participant.
        """
        return (
            (user.is_authenticated() and self.is_public)
            or (user in self.participants.all())
            or (user in self.moderators.all())
        )

    @functional.cached_property
    def other_projects(self):
        other_projects = self.organisation.project_set\
            .filter(is_draft=False).exclude(slug=self.slug)
        return other_projects

    @functional.cached_property
    def is_private(self):
        return not self.is_public

    @functional.cached_property
    def active_phase(self):
        from euth.phases import models as phase_models
        return phase_models.Phase.objects\
                                 .filter(module__project=self)\
                                 .active_phases()\
                                 .first()

    @property
    def days_left(self):
        if self.active_phase:
            today = timezone.now().replace(hour=0, minute=0, second=0)
            time_delta = self.active_phase.end_date - today
            return time_delta.days
