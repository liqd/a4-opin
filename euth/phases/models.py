from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from euth.modules import models as modules_models

from . import content
from .validators import validate_content


class PhasesQuerySet(models.QuerySet):

    def active_phases(self):
        now = timezone.now()
        return self.filter(start_date__lte=now, end_date__gt=now)


class Phase(models.Model):
    name = models.CharField(
        max_length=512,
        help_text=_('This name will appear on top of the project detail page')
    )
    description = models.TextField(
        help_text=_(
            'This is a short description of what happens in this phase')
    )
    type = models.CharField(max_length=128, validators=[validate_content])
    module = models.ForeignKey(modules_models.Module, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    objects = PhasesQuerySet.as_manager()

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)

    @property
    def view(self):
        return content[self.type].view

    def has_feature(self, feature, model):
        return content[self.type].has_feature(feature, model)
