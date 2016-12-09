from django.db import models

from euth.modules import models as module_models


class Proposal(module_models.Item):
    name = models.CharField(max_length=120)
    description1 = models.TextField()
    description2 = models.TextField()
