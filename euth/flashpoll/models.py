from django.db import models
from django.utils.translation import ugettext as _

from euth.modules import models as module_models


class Flashpoll(module_models.AbstractSettings):
    key = models.CharField(max_length=30, verbose_name=_('Flashpoll ID'))

    def __str__(self):
        return self.key
