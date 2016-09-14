from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.utils import timezone

from euth.contrib import base_models
from euth.projects import models as project_models


class Module(models.Model):
    name = models.CharField(max_length=512, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(null=True, blank=True)
    weight = models.PositiveIntegerField()
    project = models.ForeignKey(
        project_models.Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.project, self.weight)

    def phases_passed(self):
        return self.phase_set.filter(end_date__lte=timezone.now())


class Item(base_models.TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def process(self):
        return self.module.project
