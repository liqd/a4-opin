from django.db import models

from euth.modules import models as modules_models

from . import content
from .validators import validate_content


class Phase(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    type = models.CharField(max_length=128, validators=[validate_content])
    module = models.ForeignKey(modules_models.Module, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)

    @property
    def view(self):
        return content[self.type].view
