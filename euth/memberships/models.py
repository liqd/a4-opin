from django.conf import settings
from django.db import models

from euth.contrib.base_models import TimeStampedModel
from euth.projects import models as prj_models

from . import emails


class RequestManager(models.Manager):
    def request_membership(self, project, user):
        request = super().create(creator=user, project=project)
        emails.RequestReceivedEmail.send(request)
        return request


class Request(TimeStampedModel):
    """
    An requestt for joining a private project.
    """
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        prj_models.Project,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('creator', 'project')

    objects = RequestManager()

    def __str__(self):
        return "Request by {s.creator} for {s.project}".format(s=self)

    def accept(self):
        self.project.participants.add(self.creator)
        self.delete()
        emails.RequestAcceptedEmail.send(self)

    def decline(self):
        self.delete()
