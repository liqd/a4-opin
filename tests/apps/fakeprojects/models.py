from django.conf import settings
from django.db import models


class FakeProject():
    """
    Minimal set of fields expected for a project.
    """
    name = 'fakey process name'
    active_phase = None
    is_public = False

    def has_member(self, user):
        return True


class FakeProjectContent(models.Model):
    """
    Minimal set of field expected for project content.
    """
    project = FakeProject()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
