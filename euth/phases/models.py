from django.db import models

from euth.modules import models as modules_models

from . import content
from .validators import validate_content


class PhasesQuerySet(models.QuerySet):

    def active_phase(self, project):
        return self.filter(module__project=project).order_by('type').first()

    def all_phases(self, project):
        return self.filter(module__project=project).order_by('type')


class Phase(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    type = models.CharField(max_length=128, validators=[validate_content])
    module = models.ForeignKey(modules_models.Module, on_delete=models.CASCADE)

    objects = PhasesQuerySet.as_manager()

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)

    @property
    def view(self):
        return content[self.type].view

    def has_feature(self, feature, model):
        return content[self.type].has_feature(feature, model)
