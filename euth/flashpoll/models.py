from django.db import models

from euth.modules import models as module_models


class Flashpoll(module_models.Item):
    key = models.CharField(max_length=30)

    def __str__(self):
        return self.key
