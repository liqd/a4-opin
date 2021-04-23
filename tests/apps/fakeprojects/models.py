from django.conf import settings
from django.db import models

from adhocracy4.projects.enums import Access


class FakeProject():
    """
    Minimal set of fields expected for a project.
    """
    name = 'fake projects name'
    active_phase = None
    access = Access.PRIVATE

    def has_member(self, user):
        return True

    def has_moderator(self, user):
        return False


class FakeProjectContent(models.Model):
    """
    Minimal set of field expected for project content.
    """
    project = FakeProject()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
