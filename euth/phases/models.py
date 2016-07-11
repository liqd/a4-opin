from django.conf import settings
from django.db import models
from model_utils import models as model_utils

from ..projects import models as project_models


class Module(models.Model):
    weight = models.PositiveIntegerField()
    project = models.ForeignKey(project_models.Project, on_delete=models.CASCADE)
    max_identifier = models.PositiveIntegerField()

    def __str__(self):
        return "{} ({})".format(self.project, self.weight)


class Phase(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    permissions = models.CharField(max_length=128)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(model_utils.TimeStampedModel):
    identifier = models.PositiveIntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unqiue_together = (('identifier', 'module'), )

    def save(self, *args, **kwargs):
        if not self.identifier:
            module = self.module
            module.max_identifier = F('max_identifier') + 1
            module = module.save()
            self.identifier = module.max_identifier

        super(Item, self).save(*args, **kwargs)
