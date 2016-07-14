from django.conf import settings
from django.db import models
from model_utils import models as model_utils

from euth.modules import models as modules_models


class Phase(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    permissions = models.CharField(max_length=128)
    module = models.ForeignKey(modules_models.Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
