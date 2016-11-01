from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils import functional, timezone
from django.utils.translation import ugettext as _

from contrib.transforms import html_transforms
from euth.contrib import base_models, validators
from euth.organisations import models as org_models


class ProjectManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def featured(self):
        return self.filter(is_draft=False).order_by('-created')[:8]


class Project(base_models.TimeStampedModel):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(
        max_length=120,
        verbose_name=_('Title of your project'),
        help_text=_('This title will appear on the '
                    'teaser card and on top of the project '
                    'detail page. It should be max. 120 characters long')
    )
    organisation = models.ForeignKey(
        org_models.Organisation, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=120,
        verbose_name=_('Short description of your project'),
        help_text=_('This short description will appear on '
                    'the header of the project and in the teaser. '
                    'It should briefly state the goal of the project '
                    'in max. 120 chars.')
    )
    information = RichTextUploadingField(
        config_name='image-editor',
        verbose_name='Description of your project',
        help_text='This description should tell participants '
        'what the goal of the project is, how the project’s '
        'participation will look like. It will be always visible '
        'in the „Info“ tab on your project’s page.')
    result = RichTextUploadingField(blank=True, config_name='image-editor')
    is_public = models.BooleanField(
        default=True,
        verbose_name=_('Access to the project'),
        help_text=_('Please indicate who should be able to participate in '
                    'your project. Teasers for your project including title '
                    'and short description will always be visble to everyone')
    )
    is_draft = models.BooleanField(default=True)
    image = models.ImageField(
        verbose_name=_('Header image'),
        help_text=_('The image will be shown as a decorative '
                    'background image. It must be min. 1300px wide and '
                    '600px tall. Allowed file formats are .jpg and .png. '
                    'The file size should be max. 2 MB.'),
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
            self.information, 'image-editor')
        self.result = html_transforms.clean_html_field(
            self.result, 'image-editor')
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

    def has_moderator(self, user):
        return user in self.moderators.all()

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

    @property
    def phases(self):
        from euth.phases import models as phase_models
        return phase_models.Phase.objects.filter(module__project=self)

    @property
    def last_phase(self):
        phases = self.phases.filter(end_date__lt=timezone.now())
        phases_ordered = phases.order_by('end_date').last()
        return phases_ordered
