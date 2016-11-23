from django.db import models

from euth.contrib import base_models
from euth.projects import models as prj_models


class Follow(base_models.UserGeneratedContentModel):
    project = models.ForeignKey(prj_models.Project)
    enabled = models.BooleanField(default=True)

    class Meta:
        unique_together = ('project', 'creator')

    def __str__(self):
        return 'Follow({}, enabled={})'.format(self.project, self.enabled)
